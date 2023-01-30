#!/bin/bash
# shellcheck shell=bash

if [ -z "$1" ]; then
    echo "Error: URL is not provided. Please provide a valid URL as an argument when running the script."
    exit 1
fi

python get-urls.py "$1" &
wait $!

single-file \
--urls-file=urls.txt \
--browser-wait-delay=5000 \
--output-directory="$OUTPUT_DIR" \
--back-end=webdriver-gecko

rm urls.txt