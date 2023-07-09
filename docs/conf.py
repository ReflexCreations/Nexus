import os
import pathlib

import toml

root_dir = pathlib.Path(__file__).parent.parent.resolve()


def from_root(fn):
    return os.path.join(root_dir, fn)


config = toml.load(from_root("pyproject.toml"))
metadata = config.get("tool", {}).get("poetry", {})
metadata |= config.get("metadata", {})

project = metadata["title"]
author = metadata["authors"][0]
release = version = metadata["version"]
copyright = metadata["copyright"]

extensions = [
    "sphinx_rtd_theme",
]

templates_path = ["_templates"]

language = "English"

html_logo = from_root(metadata["logo"])
html_theme = "sphinx_rtd_theme"
html_static_path = ["_static"]
html_css_files = ["custom.css"]
