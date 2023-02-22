#!/bin/bash

# Assumes that `yt-dlp` is installed and on PATH and that a valid YouTube authentication cookies are present in Firefox.

# Check if YT_LISTEN_DIR environment variable is set; exit if not.
if [ -z "$YT_LISTEN_DIR" ]; then
    echo "Error: YT_LISTEN_DIR environment variable is not set."
    echo "Please set the YT_LISTEN_DIR environment variable to the path where you want to download the audio files."
    exit 1
fi

# Check if a watchlist URL was passed as an argument; if not, use the default watchlist URL.
if [ "$1" != "" ]; then
    watchlist_url="https://www.youtube.com/playlist?list=$1"
else
    watchlist_url="https://www.youtube.com/playlist?list=PL6p3R6-jA45ALhWfKrYRFagxSgYSL9SVU"
fi

# Download audio from the videos in the watchlist.
echo "Downloading audio from videos in watchlist at URL: $watchlist_url"
yt-dlp --cookies-from-browser firefox -f 'ba' -x --audio-format mp3 --yes-playlist -o "$YT_LISTEN_DIR/%(title)s.%(ext)s" "$watchlist_url"

# Run it from the root `sftm` project directory with:
# Usage: ./YT/utils/yt_dl_watchlist.sh