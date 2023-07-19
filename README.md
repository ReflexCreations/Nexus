[![][docs-badge]][Documentation] [![][lint-badge]][lint]
[![][test-badge]][test] [![][coverage-badge]][coverage] 
[![][license-badge]][LICENSE] [![][discord-badge]][discord]
[![][tag-badge]][tag] [![][pypi-badge]][pypi] 

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

[![][linux-badge]][linux] [![][macos-badge]][macos]
[![][windows-badge]][windows]

The application is stand-alone and requires no installation, so place the
executable wherever you wish to use it, and start it up.

## Documentation

For details on usage, contribution, and guides on building your own dance pad,
check out the [Documentation].

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

[coverage]: https://coveralls.io/github/ReflexCreations/Nexus?branch=main
[discord]: https://discord.gg/TCn3emnwZU
[Documentation]: https://reflex-nexus.readthedocs.io/
[LICENSE]: https://github.com/ReflexCreations/Nexus/blob/master/LICENSE
[lint]: https://github.com/ReflexCreations/Nexus/actions
[linux]: https://github.com/ReflexCreations/Nexus/releases/latest/download/reflex-nexus
[macos]: https://github.com/ReflexCreations/Nexus/releases/latest/download/reflex-nexus.tar.gz
[pypi]: https://pypi.org/project/reflex-nexus
[tag]: https://github.com/ReflexCreations/Nexus/tags
[test]: https://github.com/ReflexCreations/Nexus/actions
[windows]: https://github.com/ReflexCreations/Nexus/releases/latest/download/reflex-nexus.exe

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

[coverage-badge]: https://coveralls.io/repos/github/ReflexCreations/Nexus/badge.svg?branch=main
[discord-badge]: https://img.shields.io/discord/738700768147669088?label=discord
[docs-badge]: https://readthedocs.org/projects/reflex-nexus/badge/?version=latest
[license-badge]: https://img.shields.io/github/license/ReflexCreations/Nexus
[lint-badge]: https://img.shields.io/github/actions/workflow/status/ReflexCreations/Nexus/project-lint.yml?label=linting
[linux-badge]: https://img.shields.io/github/actions/workflow/status/ReflexCreations/Nexus/build-linux.yml?label=Linux%20Download
[macos-badge]: https://img.shields.io/github/actions/workflow/status/ReflexCreations/Nexus/build-macos.yml?label=MacOS%20Download
[pypi-badge]: https://img.shields.io/pypi/v/reflex-nexus
[tag-badge]: https://img.shields.io/github/v/tag/ReflexCreations/Nexus
[test-badge]: https://img.shields.io/github/actions/workflow/status/ReflexCreations/Nexus/project-test.yml?label=tests
[windows-badge]: https://img.shields.io/github/actions/workflow/status/ReflexCreations/Nexus/build-windows.yml?label=Windows%20Download
