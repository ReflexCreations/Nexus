[![][linux-badge]][Releases] [![][macos-badge]][Releases]
[![][windows-badge]][Releases] [![][pypi-badge]][pypi]
[![][docs-badge]][Documentation] [![][lint-badge]][lint]
[![][test-badge]][test] [![][coverage-badge]][coverage]
[![][license-badge]][LICENSE] [![][tag-badge]][tag]
[![][discord-badge]][discord]

__Note: This is a work in progress project. References made in the readme__
__and documentation are currently unfulfilled.__

# RE:Flex Nexus - Universal Dance Pad Utilities

RE:Flex Nexus aims to provide a comprehensive collection of PC software
utilities for dance pads. The interface specification is flexible, allowing
any dance pad to be quickly integrated and begin using available software
features.

In addition, the project aims to provide a comprehensive set of user guides
for open-source dance pad design. The goal is to create a centralised
ecosystem for both software tools and documentation of dance pads. This
will hopefully inspire creativity/freedom, while letting dance gamers share
technology together.

## Installation

- The latest executable can be found on the [Releases] page
- Download the application for your respective operating system
- Download the `nexus-resources.zip` package and extract to the location
you would like to store program data
- Open the `reflex-nexus` application
- You will be prompted to set up your program data folder, enter the directory
of the folder that you just extracted

## Usage

For details on usage, check out the [Documentation].

## Contributing

Install the latest version of [Python] and [git], use your terminal/command
prompt to navigate to the directory you would like to install this project to,
then run the following commands:

```bash
# Clone and enter repository.
git clone https://github.com/ReflexCreations/Nexus.git
cd nexus
# Get the build/environment manager.
pip install poetry
# Set up virtual environment and install reflex_nexus as package.
poetry install
```

You're all set up! You can now use [Poetry] to run the application scripts.

```bash
# Build the executable.
poetry run build
# Build the documentation HTML.
poetry run docs
# Lint the project.
poetry run lint
# Test the project for your Python version and operating system.
poetry run test
```

To synchronise your code editor with the virtual environment that Poetry
creates, you can use `poetry env info -p`, copy the path, and supply that path
to your code editor for the Python interpreter location.

## Acknowledgements

The following Python packages are used in this project, and are greatly
appreciated:

#### Runtime dependencies:

- [libusb-package] - Container package for libusb
- [PyQtDarkTheme] - Dark/light theme for Python QT applications
- [PySide6] - Python bindings for QT GUI framework
- [PyUSB] - Python USB access module
- [QtAwesome] - FontAwesome/Elusive Icons for Python QT applications

#### Development dependencies:

- [Poetry] - Dependency, environment and packaging manager
- [PyInstaller] - Cross-platform executable generator
- [pytest] - Project testing
- [pytest-cov] - Coverage integration for pytest
- [Ruff] - Project linting
- [Sphinx] - Documentation generator
- [Sphinx-Rtd-Theme] - Read the Docs Sphinx theme

*RE:Flex Nexus is released under the MIT License, more details in [LICENSE]
file.*

<!--- Site links -->

[coverage]: https://coveralls.io/github/ReflexCreations/Nexus
[discord]: https://discord.gg/TCn3emnwZU
[Documentation]: https://reflex-nexus.readthedocs.io/
[Git]: https://git-scm.com/downloads/
[LICENSE]: https://github.com/ReflexCreations/Nexus/LICENSE
[lint]: https://github.com/ReflexCreations/Nexus/actions/workflows/lint.yml
[Python]: https://python.org/downloads/
[pypi]: https://pypi.org/project/reflex-nexus
[Releases]: https://github.com/ReflexCreations/Nexus/releases/
[tag]: https://github.com/ReflexCreations/Nexus/tags
[test]: https://github.com/ReflexCreations/Nexus/actions/workflows/test.yml

<!--- Runtime dependency links -->

[libusb-package]: https://pypi.org/project/libusb-package/
[PyQtDarkTheme]: https://pypi.org/project/pyqtdarktheme/
[PySide6]: https://pypi.org/project/PySide6/
[PyUSB]: https://pypi.org/project/pyusb/
[QtAwesome]: https://pypi.org/project/QtAwesome/

<!--- Development dependency links -->

[Poetry]: https://pypi.org/project/poetry/
[PyInstaller]: https://pypi.org/project/pyinstaller/
[pytest]: https://pypi.org/project/pytest/
[pytest-cov]: https://pypi.org/project/pytest-cov/
[Ruff]: https://pypi.org/project/ruff/
[Sphinx]: https://pypi.org/project/Sphinx/
[Sphinx-Rtd-Theme]: https://pypi.org/project/sphinx-rtd-theme/

<!--- Badge images -->

[coverage-badge]: https://img.shields.io/coverallsCoverage/github/ReflexCreations/Nexus
[discord-badge]: https://img.shields.io/discord/738700768147669088?label=discord
[docs-badge]: https://img.shields.io/readthedocs/reflex-nexus
[license-badge]: https://img.shields.io/github/license/ReflexCreations/Nexus
[lint-badge]: https://img.shields.io/github/actions/workflow/status/ReflexCreations/Nexus/lint.yml?label=linting
[linux-badge]: https://img.shields.io/github/actions/workflow/status/ReflexCreations/Nexus/build-linux.yml?label=linux%20build
[macos-badge]: https://img.shields.io/github/actions/workflow/status/ReflexCreations/Nexus/build-macos.yml?label=macos%20build
[pypi-badge]: https://img.shields.io/pypi/v/reflex-nexus
[tag-badge]: https://img.shields.io/github/v/tag/ReflexCreations/Nexus
[test-badge]: https://img.shields.io/github/actions/workflow/status/ReflexCreations/Nexus/test.yml?label=tests
[windows-badge]: https://img.shields.io/github/actions/workflow/status/ReflexCreations/Nexus/build-windows.yml?label=windows%20build
