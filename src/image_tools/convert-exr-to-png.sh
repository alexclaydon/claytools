#!/bin/zsh
# shellcheck disable=SC1071

# Will fail if run from bash with the following error: `./src/image_tools/ref.sh:read:8: -p: no coprocess`. Accordingly disabling ShellCheck for this file as it gives misleading static analysis errors.

# Usage: im-convert-exr-png.sh [WORKING_INPUT_DIR]

# Check if the working directory is specified as a command-line argument
if [[ -n "$1" ]]; then
  working_dir="$1"
elif [[ -n "$WORKING_INPUT_DIR" ]]; then
  # Prompt the user whether to use the WORKING_INPUT_DIR environment variable or the default directory.
  read response\?"A WORKING_INPUT_DIR environment variable ($WORKING_INPUT_DIR) was found on path.  Would you like to use it? [Y/n] "
  if [[ $response =~ ^[nN] ]]; then
    echo "Ignoring the WORKING_INPUT_DIR environment variable. Using the default working directory instead."
    working_dir="$HOME/ShareDir/Renders"
  else
    working_dir="$WORKING_INPUT_DIR"
  fi
else
  working_dir="$HOME/ShareDir/Renders"
fi

echo "Working directory: $working_dir"

# Find all `.exr` files in the working directory and all of its subfolders, then convert them all to `.png` format, applying the appropriate colorspace conversions
find "$working_dir" -name "*.exr" -print | while read file; do
  echo -e "\033[32m$file\033[0m"
  convert "$file" -colorspace RGB -colorspace sRGB "${file%.*}.png"
done
