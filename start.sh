#!/usr/bin/env bash
# Open the interactive roadmap directly in your default browser
DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
open "$DIR/index.html"
