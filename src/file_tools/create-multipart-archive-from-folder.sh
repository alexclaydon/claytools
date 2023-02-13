#!/bin/zsh
# shellcheck shell=bash

# Create a multipart archive from a folder

# Set the working directory from the command line parameter or environment variable
if [[ -n "$1" ]]; then
  working_dir="$1"
else
  working_dir="$MULTIPART_ARCHIVE_WORKING_DIR"
fi

if [[ -z "$working_dir" ]]; then
  echo "Please provide the input folder as a command line argument or set the MULTIPART_ARCHIVE_WORKING_DIR environment variable."
  exit 1
fi

echo "Working directory: $working_dir"

# Check if size parameter is provided as command line argument
if [[ -z "$2" ]]; then
  echo "Please provide the size parameter (in megabytes) as a command line argument."
  exit 1
fi

size_param="$2"

# Check if password parameter is provided as a command line argument
if [[ -n "$3" ]]; then
  password="$3"
else
  password="$ZIP_PASSWORD"
fi

if [[ -z "$password" ]]; then
  echo "Please provide the password as a command line argument or set the ZIP_PASSWORD environment variable."
  exit 1
fi

# Replace any illegal characters in the directory name with legal characters
directory_name="$(basename "$working_dir")"
archive_name="$(echo "$directory_name" | tr -dc '[:alnum:]\n\r')"

# Add a timestamp to the archive name
timestamp=$(date +"%Y%m%d-%H%M%S")
archive_name="${archive_name}_${timestamp}"

# Check if archive with specified name already exists
if [[ -f "${working_dir}/${archive_name}.zip" ]]; then
  echo "An archive with the name ${archive_name}.zip already exists in the target destination. Please delete or rename the existing archive before creating a new one."
  exit 1
fi

echo "Archive filename: $archive_name"

# Create the archive with the Archive Utility and split it into parts of the specified size
cd "$working_dir" || exit 1
zip -e -r -s "${size_param}m" "${archive_name}.zip" . -P "$password" || exit 1

echo "Multipart archive created successfully."
