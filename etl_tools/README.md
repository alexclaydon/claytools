# ETL Tools

Tools for extracting, transforming, and loading data from various sources.

For development purposes, the following assumes local installation on MacOS (running on Apple Silicon), with minimal external dependencies and a simple Python venv setup.  In due course we'll add Docker development (using VS Code's `devcontainer.json`) and deployment instructions.

## External Dependencies

[Homebrew](https://brew.sh/): `/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"`

[Direnv](https://direnv.net/): `brew install direnv`

A [Python installation](https://www.python.org/) (currently, 3.9.x) from which a venv can be created.  The following assumes no particular means of installing managing your Python installation(s); we variously use [pyenv](https://github.com/pyenv/pyenv) and [asdf-vm](https://asdf-vm.com/).

An `.env` file in the form set out in `.env.sample`.

## Dagster

[Dagster](https://dagster.io/) is an open-source data orchestration tool that allows you to define and manage data pipelines as directed acyclic graphs (DAGs).

### Setup Python interpreter

On Apple Silicon Macs, currently you'll need to run Dagster in a Python 3.9 venv on account of a dependency issue with `grpcio`.  If you have any inscrutable errors during setup, chances are your venv isn't correctly activated.

After ensuring that Python 3.9.x is your current "global" interpreter, create a venv as follows:

`python -m venv .venv`

Next, install `dagster` and `dagit` as follows:

`pip install dagster dagit --find-links=https://github.com/dagster-io/build-grpcio/wiki/Wheels`

Then install other dependencies:

`pip install -r requirements.txt`

If launching from VS Code, you'll also need to set the following in environment variable to prevent `malloc` errors on launching the server:

`MallocNanoZone=1`

Also for VS Code, you should hit Cmd + P and select your new venv with `Python: Select Interpreter`.

**Additional explanation**

Regarding the `malloc` error, see [this helpful comment](https://dagster.slack.com/archives/C01U954MEER/p1671369474024709?thread_ts=1670866987.341699&cid=C01U954MEER) (requires Slack account 🙄) and [this](https://github.com/electron/electron/commit/192a7fad0d548d1883c58bdf95ab7a2ff1391881).

Google does not provide M1-compatible builds of `grpcio`, and any attempt to install `dagster` into Python 3.11 will fail for dependencies.  I've tried many solutions including the following, none of which worked:

- third party Apple Silicon build of `grpcio` from [here](https://github.com/pietrodn/grpcio-mac-arm-build/releases)
- [this](https://github.com/grpc/grpc/issues/25082)
- [this](https://stackoverflow.com/questions/66640705/how-can-i-install-grpcio-on-an-apple-m1-silicon-laptop)

While I was able to get everything up and running on Python 3.10, I continued to run into errors and eventually switched to Python 3.9.16.

### Creating a new project

The [documentation](https://docs.dagster.io/getting-started/create-new-project) suggests using `pip install dagster`, `dagster project scaffold --name my-dagster-project` to create a template project directory, then `pip install -e ".[dev]"` to install other dependencies and your definitions in pip "editable" mode.

I might try that as a greenfield project after I'm more comfortable with the tool - for instance, when bootstrapping `enviro` - I'm not sure whether I need to make adjustments to the process to handle the `grpcio` build issues I had initially getting everything up and running, so I don't want to prejudice my carefully constructed environment by wiping the slate clean.

For now, there's just one module - `global`.  Run dagster in development mode with `dagster dev -m global`.