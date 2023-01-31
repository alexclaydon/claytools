## Dagster

On account of a dependency issue with `grpcio`, currently you'll need to run Dagster in a Python 3.9 or 3.10 venv.

After creating, install `dagster` and `dagit` as follows:

`pip install dagster dagit --find-links=https://github.com/dagster-io/build-grpcio/wiki/Wheels`

Then install other dependencies:

`pip install -r requirements.txt`

If launching from VS Code, you'll also need to set the following in environment variable to prevent `malloc` errors on launching the server:

`MallocNanoZone=1`

You can then launch a server with, for example:

`dagit -f tutorial/hn_dagster.py`

## Additional explanation

Regarding the `malloc` error, see [this helpful comment](https://dagster.slack.com/archives/C01U954MEER/p1671369474024709?thread_ts=1670866987.341699&cid=C01U954MEER) (requires Slack account 🙄) and [this](https://github.com/electron/electron/commit/192a7fad0d548d1883c58bdf95ab7a2ff1391881).

Google does not provide M1-compatible builds of `grpcio`, and any attempt to install `dagster` into Python 3.11 will fail for dependencies.  I've tried many solutions including the following, none of which worked:

- third party Apple Silicon build of `grpcio` from [here](https://github.com/pietrodn/grpcio-mac-arm-build/releases)
- [this](https://github.com/grpc/grpc/issues/25082)
- [this](https://stackoverflow.com/questions/66640705/how-can-i-install-grpcio-on-an-apple-m1-silicon-laptop)

For now using 3.10 and the `grpcio` version compiled by the `dagster` team is fine.
