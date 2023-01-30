## Dependencies

The following assumes that Firefox is installed and is your browser of choice with `single-file-cli`.

Ensure that `beautifulsoup4` installed in the relevant interpreter.

Uses `wget`:

`brew install wget`

Install `single-file-cli` either globally (my preference) if you want to have it on path:

`npm install -g "single-file-cli"`

Or locally from the `web-tools` directory, in which case you'll also need to make the binary executable:

`npm install "single-file-cli"`
`chmod +x node_modules/.bin/single-file`

Then, from the `web-tools` directory, get `selenium-webdriver` and `geckodriver` for Firefox:

`npm install selenium-webdriver`
`wget -O gecko.tar.gz https://github.com/mozilla/geckodriver/releases/download/v0.32.0/geckodriver-v0.32.0-macos-aarch64.tar.gz`
`tar -xvf gecko.tar.gz`
`rm gecko.tar.gz`

Ensure all of the bash scripts in `web-tools` are executable:

`chmod +x download-all-pages.sh`

Download the URLs contained in the `urls.txt` file:

`./download-all-pages.sh`
