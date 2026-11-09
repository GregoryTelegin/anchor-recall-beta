# Third-party notices

The PolyForm Noncommercial 1.0.0 license in `LICENSE` applies to Anchor Recall's
own code. It does not replace or restrict the licenses of the third-party
components listed here. Their original permissions and notice obligations remain
in effect. This document is embedded in the generated `main.js` release bundle.

Anchor Recall bundles the following open-source packages in `main.js` to provide scheduling, local FSRS parameter optimization and Markdown formatting. They are used locally and no learning data is sent to their authors or services.

| Package | Version | License | Project |
| --- | ---: | --- | --- |
| `marked` | 18.1.1 | MIT, Markdown notice below | https://github.com/markedjs/marked |
| `ts-fsrs` | 5.4.1 | MIT | https://github.com/open-spaced-repetition/ts-fsrs |
| `@open-spaced-repetition/binding` | 0.5.0 | MIT | https://github.com/open-spaced-repetition/ts-fsrs |
| `@open-spaced-repetition/binding-wasm32-wasi` | 0.5.0 | MIT | https://github.com/open-spaced-repetition/ts-fsrs |
| `@napi-rs/wasm-runtime` | 1.2.3 | MIT | https://github.com/napi-rs/napi-rs |
| `@emnapi/core`, `@emnapi/runtime`, `@emnapi/wasi-threads` | 1.x | MIT | https://github.com/toyobayashi/emnapi |
| `@tybys/wasm-util` | 0.10.3 | MIT | https://github.com/toyobayashi/wasm-util |
| `tslib` | 2.8.1 | 0BSD | https://github.com/microsoft/tslib |

## MIT License text

Copyright belongs to the respective package authors and contributors. The
following original notices accompany the shared MIT terms below:

- `marked` (installed package `LICENSE`):

  Copyright (c) 2018+, MarkedJS (https://github.com/markedjs/)

  Copyright (c) 2011-2018, Christopher Jeffrey (https://github.com/chjj/)

- `ts-fsrs`, `@open-spaced-repetition/binding`, and `@open-spaced-repetition/binding-wasm32-wasi` (installed package `LICENSE` files):

  Copyright (c) 2026 Open Spaced Repetition

- `@emnapi/core`, `@emnapi/runtime`, and `@emnapi/wasi-threads` (installed package `LICENSE` files):

  Copyright (c) 2021-present Toyobayashi

- `@napi-rs/wasm-runtime` (MIT declared in the installed package; notices from the [upstream NAPI-RS license](https://github.com/napi-rs/napi-rs/blob/main/LICENSE)):

  Copyright (c) 2020-present LongYinan

  Copyright (c) 2018 GitHub

- `@tybys/wasm-util` declares MIT and author `toyobayashi` in its installed package metadata. Copyright remains with its authors and contributors.

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

## 0BSD text (`tslib`)

Copyright (c) Microsoft Corporation.

Permission to use, copy, modify, and/or distribute this software for any purpose with or without fee is hereby granted.

THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.

## Markdown notice (included with `marked`)

Copyright © 2004, John Gruber
http://daringfireball.net/
All rights reserved.

Redistribution and use in source and binary forms, with or without modification, are permitted provided that the following conditions are met:

* Redistributions of source code must retain the above copyright notice, this list of conditions and the following disclaimer.
* Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the following disclaimer in the documentation and/or other materials provided with the distribution.
* Neither the name “Markdown” nor the names of its contributors may be used to endorse or promote products derived from this software without specific prior written permission.

This software is provided by the copyright holders and contributors “as is” and any express or implied warranties, including, but not limited to, the implied warranties of merchantability and fitness for a particular purpose are disclaimed. In no event shall the copyright owner or contributors be liable for any direct, indirect, incidental, special, exemplary, or consequential damages (including, but not limited to, procurement of substitute goods or services; loss of use, data, or profits; or business interruption) however caused and on any theory of liability, whether in contract, strict liability, or tort (including negligence or otherwise) arising in any way out of the use of this software, even if advised of the possibility of such damage.
