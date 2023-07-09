import toml

with open("../../pyproject.toml") as f:
    pyproject = toml.load(f)

metadata = pyproject["tool"]["poetry"]
project = metadata["description"]
author = metadata["authors"][0]
release = metadata["version"]
copyright = "2023, Impulse Creations, Ltd."

extensions = []

templates_path = ['_templates']
exclude_patterns = []

language = 'English'

html_theme = 'alabaster'
html_static_path = ['_static']
