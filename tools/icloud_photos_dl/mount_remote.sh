#!/bin/zsh
# shellcheck shell=bash

# Assuming the remote volume you want is already mounted, you can use `df -P` on the MacOS command line to list all currently mounted volumes, including remote volumes, to obtain the address below.

# Define the remote server and share
remote_server="MBA13.local"
remote_share="Cold%201"

# Define the local mount point
local_mount="/Volumes/"

# Define the username and password for the remote server
username=$REMOTE_USERNAME
# password="password"

# Mount the remote share
# Variant with password
# mount_smbfs "smb://$username:$password@$remote_server/$remote_share" $local_mount
mount_smbfs "smb://$username@$remote_server/$remote_share" "$local_mount"