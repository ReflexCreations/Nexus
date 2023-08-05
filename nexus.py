"""Main entry scripts for RE:Flex Nexus project."""
import pathlib
import subprocess
import sys

from src.app.application import Application


def app() -> None:
    """Run application from source."""
    sys.exit(Application().run())


def build() -> int:
    """Build application executable."""
    script = ["pyinstaller", "nexus.spec"]
    return subprocess.run(script).returncode


def cover() -> int:
    """Create coverage report for coveralls."""
    script = ["coverage", "xml"]
    return subprocess.run(script).returncode


def docs() -> int:
    """Build Sphinx documentation for project."""
    script = ["sphinx-build", "-E", "-a", "-b", "html", "docs/", "docs/build"]
    return subprocess.run(script).returncode


def lint() -> int:
    """Run linter on project."""
    script = ["ruff", "check", ".", "--output-file", "lint.txt"]
    return subprocess.run(script).returncode


def test() -> int:
    """Run unit tests on project, with context of source coverage."""
    def is_valid_dir(p: pathlib.Path) -> bool:
        if not p.is_dir() or p.name.startswith("_") or p.name.startswith("."):
            return False
        return True
    source = pathlib.Path(__file__).parent / "src"
    paths = [f"--cov={p}" for p in source.rglob('*') if is_valid_dir(p)]
    script = ["pytest", "--junitxml=test.xml", *paths]
    return subprocess.run(script).returncode


if __name__ == "__main__":
    app()
