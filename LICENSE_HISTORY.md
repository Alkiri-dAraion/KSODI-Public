# Licence Decision History

This file records the reason for the repository's licence changes. It is a provenance note, not a separate licence.

## Current decision — 24 July 2026

The published KSODI method documentation and method materials in this repository are licensed under the [Creative Commons Attribution 4.0 International licence](./LICENSE.md), unless a file or subfolder in this repository explicitly states otherwise.

This restores CC BY 4.0 at the repository root. The decision separates two different kinds of work:

- **Method documentation and research material:** CC BY 4.0 permits copying, sharing, adaptation, forks, experimentation and commercial use, provided the required attribution is retained, modifications are indicated and the licence is referenced.
- **Software implementation:** executable code is a separate work and may use a software licence. This repository may later contain a very small observer-orientation note or minimal implementation guidance, but implementation is not its focus and such material should not be treated as a production-ready software implementation. As of July 2026, a beta implementation of KSODI Standard-Eval is expected in approximately two to three months, possibly sooner, in [Patrick Barthelmäs's GitHub account](https://github.com/blackbaddl13). That implementation is currently expected to use the MIT License. Its own repository and licence file will be authoritative when it is published.

The separation reflects the actual division of work: this repository defines and documents the KSODI method and may provide limited implementation orientation; Patrick develops the executable software implementation separately. A software-oriented MIT licence is therefore useful for implementation repositories, but it is not the appropriate replacement for attribution-based licensing of the method documentation.

Contribution roles are documented separately in [Contributors.md](./Contributors.md).
The development timeline records milestones and provenance; it is not a full
authorship or rights definition. The repository-level method citation is
defined by `CITATION.cff`; layer-specific notices such as KSODI-Light
attribution and separately licensed executable implementations should be cited
and licensed according to their own repository files.

Research, testing, forks, adaptations and contributions are welcome. CC BY 4.0 does not require contributions to be returned upstream, but it does require attribution when the licensed material is shared and requires changes to be indicated.

## Previous interim decision — 12 February 2026

On 12 February 2026, the repository was split into differently licensed areas. CC BY 4.0 was limited to KSODI-Light, while Standard-Eval and KSODI-Full were reserved. At that time, a software-oriented licensing path, including MIT for a future implementation, was still being considered without a fully settled boundary between method documentation and implementation code.

The conservative interim split prevented an unclear licence from being applied across unfinished evaluation and implementation layers. The decision of 24 July 2026 supersedes that active split because the boundary is now explicit: method documentation in this repository is licensed under CC BY 4.0; separately published implementation code may use MIT or another software licence defined by its own repository.

The former root notice was:

```text
Multi Licence Notice

This repository contains component under different licences.
Please refer to the licence file inside each folder.
```

The former active notice in `KSODI-Eval-Variants/LICENSE.md` was:

```text
(C) Copyright 2026 Anne Steinacker-Folkerts and Heiko Folkerts

All rights reserved.

The material in this folder and its subfolders may not be used, copied, used, modified, distributed, published, sublicensed or commercialy exploited without prior written permission form the authors.

For licence inquiries please contact:
ksodi@thevoid.email
```

Both notices are retained here to preserve the repository's licence provenance. They no longer define the active licence of the published KSODI method materials.
