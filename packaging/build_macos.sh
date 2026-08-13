#!/bin/bash
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"

if [ ! -x .venv/bin/python ]; then
  echo "Cybertron build error: expected .venv/bin/python"
  echo "Build the official Big Sur release from the same working environment used to run Cybertron."
  exit 1
fi

PY="$ROOT/.venv/bin/python"

"$PY" -m pip install --upgrade "pyinstaller>=6.21,<7"
rm -rf build dist

"$PY" -m PyInstaller \
  --noconfirm \
  --clean \
  --windowed \
  --onedir \
  --name Cybertron \
  --osx-bundle-identifier com.josephdola.cybertron \
  --add-data "voice/browser_bridge.html:voice" \
  main.py

if [ ! -d dist/Cybertron.app ]; then
  echo "Cybertron.app was not created."
  exit 1
fi

rm -f dist/Cybertron-macOS-x86_64.dmg
hdiutil create \
  -volname "Cybertron" \
  -srcfolder dist/Cybertron.app \
  -ov \
  -format UDZO \
  dist/Cybertron-macOS-x86_64.dmg

echo "Built dist/Cybertron.app"
echo "Built dist/Cybertron-macOS-x86_64.dmg"
