---
title: Wiki Readme
status: wiki
tags:
  - wiki
  - github-wiki
  - publishing
  - sync
---

# Wiki Readme

This directory is the human-readable wiki surface for the schema corpus.

GitHub wikis are separate git repositories. The intended workflow is:

1. maintain canonical source pages here under `docs/wiki/`
2. sync those pages into `<repo>.wiki.git`
3. keep canonical architecture truth in the main repo, not only in the wiki

Use [../../scripts/publish_wiki.sh](../../scripts/publish_wiki.sh) as the local starting point for wiki sync and inspection.

