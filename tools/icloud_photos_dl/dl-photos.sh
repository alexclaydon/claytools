#!/bin/zsh
# shellcheck shell=bash

icloudpd \
--directory "$TARGET_DIR" \
--username "$USER_NAME" \
"$@"