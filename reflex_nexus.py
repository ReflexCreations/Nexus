"""Main entry scripts for RE:Flex Nexus project."""

import subprocess
import sys

from src.app.application import Application


def app() -> None:
    """Run application from source."""
    sys.exit(Application().run())


def build() -> int:
    """Build application executable."""
    script = ["pyinstaller", "reflex_nexus.spec"]
    return subprocess.run(script).returncode


def docs() -> int:
    """Build Sphinx documentation for project."""
    script = ["sphinx-build", "-E", "-a", "-b", "html", "docs/", "docs/build"]
    return subprocess.run(script).returncode


def lint() -> int:
    """Run linter on project."""
    script = ["ruff", "check", "."]
    return subprocess.run(script).returncode


def test() -> int:
    """Run unit tests on project."""
    script = ["pytest", "--cov=."]
    return subprocess.run(script).returncode


if __name__ == "__main__":
    app()
