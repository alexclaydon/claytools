#!/bin/zsh
# shellcheck shell=bash

if [ $# -eq 1 ]; then
  target_dir="$1"
elif [ -z "$AUTOSHOT_TARGET_DIR" ]; then
  echo "Error: Target directory not specified. Use either command line argument or AUTOSHOT_TARGET_DIR environment variable."
  exit 1
else
  target_dir="$AUTOSHOT_TARGET_DIR"
fi

if [ ! -d "$target_dir" ]; then
  echo "Error: Target directory does not exist."
  exit 1
fi

filename="$target_dir/AutoShot-$(date +%Y%m%d-%H%M%S).png"

/usr/sbin/screencapture "$filename"
