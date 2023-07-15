![][docs-badge] ![][license-badge] ![][coverage-badge] ![][tag-badge]
![][linux-badge] ![][macos-badge] ![][windows-badge] ![][discord-badge]


# RE:Flex Nexus - Universal Dance Pad Utilities

RE:Flex Nexus aims to provide a comprehensive collection of PC software
utilities for dance pads. The interface specification is flexible, allowing
any dance pad to be quickly integrated and begin using available software
features.

## Installation

- The latest executable can be found on the [Releases] page
- Download the application for your respective operating system
- Download the `nexus_resources.zip` package and extract to the location
you would like to store program data
- Open the `reflex_nexus` application
- You will be prompted to set up your program data folder, enter the directory
of the folder that you just extracted

## Documentation

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
- [PyUSB] - Facilitates communication with USB peripherals
- [QtAwesome] - FontAwesome/Elusive Icons for Python QT applications

#### Development dependencies:

- [Poetry] - Dependency manager
- [PyInstaller] - Cross-platform executable generator
- [Ruff] - Project linting
- [Sphinx] - Documentation generator
- [Sphinx-Rtd-Theme] - Read the Docs Sphinx theme

*RE:Flex Nexus is released under the MIT License, more details in [LICENSE]
file.*

<!--- Site links -->

[Documentation]: https://reflex-nexus.readthedocs.io/
[Git]: https://git-scm.com/downloads/
[LICENSE]: https://github.com/ReflexCreations/Nexus/LICENSE
[Python]: https://python.org/downloads/
[Releases]: https://github.com/ReflexCreations/Nexus/releases/

<!--- Project dependency links -->

[libusb-package]: https://pypi.org/project/libusb-package/
[PyQtDarkTheme]: https://pypi.org/project/pyqtdarktheme/
[PySide6]: https://pypi.org/project/PySide6/
[PyUSB]: https://pypi.org/project/pyusb/
[QtAwesome]: https://pypi.org/project/QtAwesome/

<!--- Development dependency links -->

[Poetry]: https://pypi.org/project/poetry/
[PyInstaller]: https://pypi.org/project/pyinstaller/
[Ruff]: https://pypi.org/project/ruff/
[Sphinx]: https://pypi.org/project/Sphinx/
[Sphinx-Rtd-Theme]: https://pypi.org/project/sphinx-rtd-theme/

<!--- Badge links -->

[coverage-badge]: https://img.shields.io/coverallsCoverage/github/ReflexCreations/Nexus
[discord-badge]: https://img.shields.io/discord/738700768147669088
[docs-badge]: https://img.shields.io/readthedocs/reflex-nexus
[license-badge]: https://img.shields.io/github/license/ReflexCreations/Nexus
[linux-badge]: https://img.shields.io/github/actions/workflow/status/ReflexCreations/Nexus/linux-pipeline?label=linux
[macos-badge]: https://img.shields.io/github/actions/workflow/status/ReflexCreations/Nexus/macos-pipeline?label=macos
[tag-badge]: https://img.shields.io/github/v/tag/ReflexCreations/Nexus
[windows-badge]: https://img.shields.io/github/actions/workflow/status/ReflexCreations/Nexus/windows-pipeline?label=windows
