#!/bin/bash

# Diffusers creates a pickle file with the file name as the root directory.
# This trips the WebUI's pickle checker which expects the root directory to be
# named "archive". This script renames the root directory to "archive".

if [ -z "$1" ]; then echo -e "Usage:\n./fix-diffusers-root-directory.sh [file or directory of files]" && exit 1; fi
TARGET_PATH="$1"

# Prompt the user to install 7zip if they don't have it insalled
if [ $(dpkg-query -W -f='${Status}' p7zip-full 2>/dev/null | grep -c "ok installed") = 0 ]; then
    sudo apt update && sudo apt install p7zip-full
fi

TMP=$(mktemp -d)

test_zip () {
  unzip -l "$1"
  return $?
}

do_convert () {
  TARGET_FILE="$1"
  FILENAME=$(basename "$TARGET_FILE")
  NAME="${FILENAME%.*}"
  EXT="${FILENAME##*.}"

  7z x "$TARGET_FILE" -o"$TMP"

  # There should only be one file in this tmp directory.
  # We don't know what its name is so we will do one loop
  # which will be only our target directory.
  for file in "$TMP"/*; do
    mv "$file" "$TMP/archive"
    NEW_NAME="${NAME}_fixed.zip"
    7z a -tzip -mx=9 "${NAME}_fixed.$EXT" "$TMP/archive"
    break
  done
}

if [ -d "$TARGET_PATH" ]; then
  for file in "$TARGET_PATH"/*; do
    if [ -f "$file" ] && test_zip "$file"; then
      do_convert "$file"
    fi
  done
else
  if test_zip "$TARGET_PATH"; then
    do_convert "$TARGET_PATH"
  fi
fi

rm -rf "$TMP"
