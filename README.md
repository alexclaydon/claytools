# claytools

All of these tools are grouped together under a single `claytools` repo and VS Code workspace for a number of reasons - not least of which is that they share documentation and a lot of code, including many of the same libraries.

On account of the way VS Code handles multiple Python interpreters (and multiple environments generally) in a single workspace, note the following:

- Tools are arbitrarily grouped together under folders, both because they can easily share a venv, and for reasons of legibility and convenience.
- Currently, there is a main workspace Python interpreter, located at `claytools/.venv`, which is used - by default set in the `.code-workspace` file - by many tools in the repo.  Going forward I expect this to be less and less relevant as tools and groups of tools get their own interpreters.
- Some tools - or groups of tools - have special requirements, such as older versions of Python, or a pinned version of some dependency that may be inconsistent with the needs of other tooling using a shared interpreter.
- Those tools have their own venv, located at `$TOOL_SUBFOLDER/.venv`.  To ensure that any new terminal launched _inside of VS Code_ (we will handle external terminals separately below) in service of invoking those tools uses the correct Python interpreter, we need to treat each group of tools and its interpreter as its own workspace root; accordingly, this is a multi-root workspace.
- Once a group has been added as its own workspace root using `File` -> `Add Folder to Workspace`, you need to set the relevant Python interpreter by navigating to that root and going through the command palette: Cmd + P, then > then `Python: Select Interpreter`, then choosing the relevant venv.  For whatever reason, _VS Code does not expose, nor does it allow you to set, the interpreter through the `settings.json` file, or the Settings UI, for that folder (The `python.defaultInterpreterPath` setting is for the workspace level only - placing it in a folder-level `settings.json` will have no effect).  You must do it through the command palette.  The setting for that folder is then stored internally by VS Code in an SQLite database - not, unfortunately, in the `.code-workspace` file.  You only need to do once each time a folder is added as its own workspace root.
- Note that this also helps with legibility, since you can be sure that if a particular tool or group of tools doesn't have its own distinct workspace root, it can be invoked using the default interpreter and all of the dependencies should already be in place.
- The same process should work for other languages and environments, too - e.g., Node and `npm install`.

## Dependencies

All of the instructions in this repo assume that `direnv` is being used.  If you choose not to use it, you'll need to handle your shell environments manually - including correct Python interpreter activation - particularly for terminals outside of VS Code.

- `brew install direnv`

To enable optional [direnv](https://direnv.net) support for `.env` files, as used in this repo, you should also ensure that there exists a `$HOME/.config/direnv/direnv.toml` with the `load_dotenv = true` variable set and, optionally, a full-repo whitelist.

Finally, ensure that the following is present in each relevant `.env` file for automatic interpreter activation for any external terminal thanks to `direnv`:

```sh
VIRTUAL_ENV=.venv
PATH=.venv/bin:$PATH
```

Next, install other non-Python dependencies:

- `brew install pandoc`
- `brew install librsvg`
- `brew install --cask basictex`
- `sudo tlmgr update --self`
- `sudo tlmgr install collection-fontsrecommended`

## Main Workspace Python Interpreter

- `python -m venv .venv`
- `pip install -e .`

Note that I was initially using `pip install -r requirements.txt` to install dependencies, but have since moved to include a `pyproject.toml` file, consistent with modern Python packaging recommendations.

See [Configuring setuptools using `pyproject.toml` files](https://setuptools.pypa.io/en/latest/userguide/pyproject_config.html) and [Development Mode (a.k.a. "Editable Installs")](https://setuptools.pypa.io/en/latest/userguide/development_mode.html).

## Other Workspace Python Interpreters

Instructions for tool-specific interpreters can be found in the `README.md` file under the relevant subfolder.

## Architecture

To be documented at `ARCHITECTURE.md`, with C4 charts at `ARCHITECTURE.d2`.
