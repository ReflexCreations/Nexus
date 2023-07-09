# RE:Flex Nexus - Universal Dance Pad Utilities

RE:Flex Nexus aims to provide a comprehensive collection of PC software
utilities for dance pads. The interface specification is flexible, allowing
any dance pad to be quickly integrated and begin using the features.

## Installation

- The latest executable can be found on the [Releases] page
- Download the application for your respective operating system
- Download the ``nexus_resources.zip`` package and extract to the location
you would like to store program data
- Open the `nexus` application
- You will be prompted to set up your program data folder, enter the directory
of the folder that you just extracted

## Documentation

For details on usage and development, check out the [Documentation].

## Setup - Development

Install the latest version of [Python] and [git], use your terminal/command
prompt to navigate to the directory you would like to install this project to,
then run the following commands in your terminal/command prompt:

```bash
# Clone and enter repository
git clone https://github.com/ReflexCreations/Nexus.git
cd nexus
# Get the build/environment manager
pip install poetry
# Set up the virtual environment
poetry install
# Run the application
poetry run app
# Build the executable
poetry run build
# Build the documentation HTML
poetry run docs
# Lint the project
poetry run lint
```

To synchronise your code editor with the virtual environment that Poetry
creates, you can use `poetry env info -p`, copy the path, and supply that path
to your code editor for the Python interpreter location.

## Acknowledgements

The following Python packages are used in this project, and are greatly
appreciated:

*Runtime dependencies*
- [libusb-package] - Container package for libusb
- [PySide6] - Python bindings for QT GUI framework
- [PyUSB] - Facilitates communication with USB peripherals
- [PyQtDarkTheme] - Dark/light theme for Python QT applications
- [QtAwesome] - FontAwesome/Elusive Icons for Python QT applications

*Development dependencies*
- [Poetry] - Dependency manager
- [PyInstaller] - Cross-platform executable generator
- [Ruff] - Project linting
- [Sphinx] - Documentation generator

*RE:Flex Nexus is released under the MIT License, more details in [LICENSE]
file.*

[Documentation]: https://readthedocs.org
[Releases]: https://github.com/ReflexCreations/Nexus/releases
[LICENSE]: https://github.com/ReflexCreations/Nexus/LICENSE
[Python]: https://python.org/downloads
[Git]: https://git-scm.com/downloads

[Ruff]: https://pypi.org/project/ruff/
[PyInstaller]: https://pypi.org/project/pyinstaller/
[Sphinx]: https://pypi.org/project/Sphinx/
[Poetry]: https://pypi.org/project/poetry/

[libusb-package]: https://pypi.org/project/libusb-package/
[PySide6]: https://pypi.org/project/PySide6/
[PyUSB]: https://pypi.org/project/pyusb/
[PyQtDarkTheme]: https://pypi.org/project/pyqtdarktheme/
[QtAwesome]: https://pypi.org/project/QtAwesome/
