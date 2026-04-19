#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
WIKI_SRC="$ROOT/docs/wiki"

echo "Wiki source directory: $WIKI_SRC"
echo "This repo is wiki-ready."
echo "To publish to a GitHub wiki, sync the files in docs/wiki to the <repo>.wiki.git repository."
echo "Canonical pages:"
find "$WIKI_SRC" -maxdepth 1 -type f | sort

