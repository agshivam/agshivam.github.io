#!/usr/bin/env bash
# Build the site and copy the result to the repo root, which is what GitHub Pages serves.
set -euo pipefail
cd "$(dirname "$0")"
cp ../Shivam-Agarwal-Resume.pdf public/Shivam-Agarwal-Resume.pdf
npm install --silent
npm run build
rm -rf ../assets ../shots
cp -R ../dist/assets ../dist/shots ../dist/index.html ../dist/Shivam-Agarwal-Resume.pdf ..
echo "Site files updated in the repo root. Commit and push to publish."
