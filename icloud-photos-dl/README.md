This is a convenience wrapper around the iCloud PD CLI.

## Setup

Requires Python 3.9.  I'm using 3.9.16, the most recent version of 3.9.  Ensure that 3.9 is activated (for example, using `pyenv global 3.9`) before creating your `venv`:

```bash
python -m venv .venv
pip install -r requirements.txt
```

## Auth

See project documentation [here](https://github.com/icloud-photos-downloader/icloud_photos_downloader/blob/master/README.md).

The script looks for the two environment variables referred to in `env.sample`: `USER_NAME` (the iCloud account username) and `TARGET_DIR` (the target download directory).

You can add the iCloud account password to MacOS Keyring using the `iCloud` CLI utility.  It will then be visible in the Keychain Access app as `pyicloud://icloud-password`.  The `dl-photos.sh` script can then be run headless.  The stores password can be removed at any time using `icloud --username $USERNAME --delete-from-keyring`.

## Usage

After ensuring that the correct Python environment is activated, call the script using: `./dl-photos.sh`.  By default all photos will be downloaded to the specified target directory.  Alternatively, the script will pass through any additional parameters to `icloudpd`; for example: `./dl-photos.sh --recent 1000 --skip-videos`.
