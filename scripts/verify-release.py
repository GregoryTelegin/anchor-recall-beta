"""The distribution repository publishes verified bytes; it never rebuilds private sources."""
from hashlib import sha256
from pathlib import Path
import json
import re
import sys
import zipfile

root = Path(__file__).resolve().parent.parent

def verify(tag, directory=root):
    directory = Path(directory)
    if not re.fullmatch(r"[0-9]+\.[0-9]+\.[0-9]+", tag):
        raise ValueError("Invalid release tag")
    meta = json.loads((directory / "BUILD.json").read_text(encoding="utf-8"))
    manifest = json.loads((directory / "manifest.json").read_text(encoding="utf-8"))
    if tag != meta["version"] or tag != manifest["version"] or manifest["id"] != "anchor-recall" or manifest.get("isDesktopOnly") is not True:
        raise ValueError("Release tag, manifest and verified build do not match")
    expected = {"main.js", "manifest.json", "styles.css", "LICENSE", "THIRD_PARTY_NOTICES.md", "TESTER-ru.md", "AnchorRecall-0.1.0.zip"}
    if set(meta["sha256"]) != expected:
        raise ValueError("Unexpected release payload")
    for name, digest in meta["sha256"].items():
        path = directory / name
        if path.is_symlink() or sha256(path.read_bytes()).hexdigest() != digest:
            raise ValueError("Frozen asset differs: " + name)
    expected_zip = {"anchor-recall/main.js", "anchor-recall/manifest.json", "anchor-recall/styles.css", "LICENSE", "THIRD_PARTY_NOTICES.md", "README.md", "TESTER-ru.md", "BUILD.json"}
    with zipfile.ZipFile(directory / "AnchorRecall-0.1.0.zip") as archive:
        if len(archive.namelist()) != len(expected_zip) or set(archive.namelist()) != expected_zip or archive.testzip() is not None:
            raise ValueError("Unexpected or damaged archive")
        original = json.loads(archive.read("BUILD.json"))
        if original["buildId"] != meta["buildId"]:
            raise ValueError("Archive build identifier differs")
        for name in expected - {"AnchorRecall-0.1.0.zip"}:
            key = "anchor-recall/" + name if name in {"main.js", "manifest.json", "styles.css"} else name
            if archive.read(key) != (directory / name).read_bytes():
                raise ValueError("Standalone asset differs from archive: " + name)
    sums = "".join(f"{meta['sha256'][name]}  {name}\n" for name in sorted(expected))
    if (directory / "SHA256SUMS.txt").read_text(encoding="utf-8") != sums:
        raise ValueError("Checksum listing differs")
    return {"version": tag, "buildId": meta["buildId"], "verifiedFiles": len(expected)}

if __name__ == "__main__":
    print(json.dumps(verify(sys.argv[1])))
