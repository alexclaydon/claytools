# Readme

Last updated: 1 January 2023

## Installing Python

- Note that each of the Win10 PC, MBP14 and MBA13 have their own venv, installed into the `.venv` directory, which is excluded from Syncthing.
- Use `python -m venv .venv` to create the venv; don't bother with VS Code auto-creation using `Python: Create Environment`, since it seems to intermittently not pick up the global python interpreter managed by `pyenv`.
- Do not succumb to suggestions to use `virtualenv` (or `pyenv-virtualenv`) to create your virtual environments; stick the with the standard library-available `venv` on all platforms. 

### Windows

- Installed Python from the Microsoft store, then used `venv` (`python -m venv .venv`) to create a venv in this repo.
- However, see [this](https://stackoverflow.com/questions/69605313/vs-code-terminal-activate-ps1-cannot-be-loaded-because-running-scripts-is-disa) error concerning the use of Powershell as your integrated terminal.  I got around this by adding: `"terminal.integrated.defaultProfile.windows": "Command Prompt"` to my VS Code `settings.json` (also taking care to then delete the current Powershell instance from the integrated Terminal window and replace it with Command Prompt, then reload VS Code).

### MacOS

- On MBA13 I installed Python using `asdf`, ensured that it was the global Python, then created a venv (`python -m venv .venv`) in the local copy of this repo.  I'm not sure I would bother using `asdf` again.
- On MBP14, installed Python using `pyenv`, then set it to the global Python, then created a venv in the local copy of this repo (`python -m venv .venv`).

#### Non-Python dependencies

`brew install yt-dlp`

### Selecting interpreter for editor and terminal

- Once the venv is created, you can select the interpreter for the editor by clicking on the Python version in the bottom right of the editor window, then selecting the interpreter from the list.
- However, for some reason the Terminal was not automatically activating the venv.  It's not clear to me why.  I have updated global workspace settings to attempt to address this but in any event, have manually checked each machine and made sure that the Terminal is now using the correct interpreter.

### Installing packages

Once confirming that the correct venv is activated, `pip install -r requirements.txt`.

## Building API docsets for Dash and Zeal

Documentation on building docsets is [here](https://kapeli.com/docsets#python).

Note that while `doc2dash` is installed into each venv, it is also installed as a binary on the Windows system, and I will also install it on the pyenv-enabled global python on the Macs, just to enable more convenient generation of docsets from any path.

### Blender

- Download the Python API documentation [here](https://docs.blender.org/api/current/index.html) (direct link to [3.4.1](https://docs.blender.org/api/current/blender_python_reference_3_4.zip))
- As the documents are Sphinx-compatible, generate them with [doc2dash](https://github.com/hynek/doc2dash).  Note that `doc2dash` binaries are available, but I've also added it to the `requirements.txt` file in this repo should you want to build with the local interpreter.
- For now: `doc2dash blender_python_reference_3_4`.
- As of today, the docset is installed on only MBP14.

### Unreal Engine

- A local copy of both the Blueprint and C++ API documentation (which forms the basis for the Python API) is installed with the engine, located at `Epic Games/UE_5.1/Engine/Documentation/Builds`
- I've extracted the UE5.1 documentation to a tree of HTML files, but haven't yet built a docset from it; have a look at [this](https://kapeli.com/docsets#dashDocset) for options.
- There is also separate documentation for the actual Python API [here](https://docs.unrealengine.com/5.1/en-US/PythonAPI/), although it is not available locally.  #TODO: I'd like to get that into a docset at some point.
