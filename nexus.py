import subprocess
import sys

from src.app.application import Application


def app():
    sys.exit(Application().run())


def build():
    script = ["pyinstaller", "nexus.spec"]
    subprocess.run(script)


def docs():
    script = ["sphinx-build", "-E", "-a", "-b", "html", "docs/", "docs/build"]
    subprocess.run(script)


def lint():
    script = ["ruff", "check", "."]
    subprocess.run(script)


if __name__ == "__main__":
    app()
