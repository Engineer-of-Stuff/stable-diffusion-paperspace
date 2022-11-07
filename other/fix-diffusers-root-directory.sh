#!/bin/bash

# Diffusers creates a pickle file with the file name as the root directory.
# This trips the WebUI's pickle checker which expects the root directory to be
# named "archive". This script renames the root directory to "archive".

if [ -z "$1" ]; then echo -e "Usage:\n./fix-diffusers-root-directory.sh [file or directory of files]" && exit 1; fi
TARGET_PATH="${@%/}"

test_zip () {
  if file "$1" | grep "Zip archive" > /dev/null 2>&1; then
    return 0
  else
    return 1
  fi
}

do_convert () {
  TARGET_FILE="$1"
  FILENAME=$(basename "$TARGET_FILE")
  NAME="${FILENAME%.*}"
  EXT="${FILENAME##*.}"
  NEW_NAME="${NAME}_fixed.$EXT"
  echo "$TARGET_FILE -> $NEW_NAME"
  # Passing the file back through torch seems to fix it
  python3 -c "import torch; torch.save(torch.load('$TARGET_FILE', map_location='cpu'), '$NEW_NAME')"
}

if [ -d "$TARGET_PATH" ]; then
  for file in "$TARGET_PATH"/*; do
    if [ -f "$file" ] && test_zip "$file"; then
      do_convert "$file"
    fi
  done
else
  for file in $TARGET_PATH; do
    if test_zip "$file"; then
      do_convert "$file"
    fi
  done
fi
