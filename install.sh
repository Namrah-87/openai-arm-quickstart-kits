#!/usr/bin/env bash

set -e

echo "=== OpenAI ARM Quickstart Kits Installer ==="

# Ensure Python exists
if ! command -v python3 >/dev/null 2>&1; then
    echo "Python3 is required but not installed."
    echo "Please install Python3 and rerun this installer."
    exit 1
fi

# Download the Python installer to a temp file
TMPFILE=$(mktemp)
curl -sSL https://raw.githubusercontent.com/<YOUR-USERNAME>/<YOUR-REPO>/main/install.py -o "$TMPFILE"

# Run the installer
python3 "$TMPFILE"

# Cleanup
rm "$TMPFILE"
