#!/bin/zsh
# shellcheck shell=bash

# Usage: im-convert-exr-png.sh [IMAGE_WORKING_DIR]

#  Set the working directory in the following order of precedence: (i) command line parameter, (ii) environment variable, (iii) default.

if [[ -n "$1" ]]; then
  working_dir="$1"
else
  working_dir="$IMAGE_WORKING_DIR"
  if [[ -z "$IMAGE_WORKING_DIR" ]]; then
    working_dir="$HOME/ShareDir/Renders"
  fi
fi

echo "Working directory: $working_dir"

# Find all `.exr` files in the working directory and all of its subfolders

find "$working_dir" -name "*.exr" -print | while read file; do
  echo -e "\033[32m$file\033[0m"
done

# Convert all `.exr` files returned by the above `find` command to `.png` format, applying the appropriate colorspace conversions

find "$working_dir" -name "*.exr" -print | while read file; do
  echo -e "\033[32m$file\033[0m"
  convert "$file" -colorspace RGB -colorspace sRGB "${file%.*}.png"
done