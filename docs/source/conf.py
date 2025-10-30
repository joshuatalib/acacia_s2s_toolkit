# Configuration file for the Sphinx documentation builder.

import tomllib  # Use 'import tomllib' if using Python 3.11+
from pathlib import Path
import sphinx_rtd_theme
import os

# -- Project information

project = 'AI_Weather_Quest'
copyright = '2025, Joshua Talib + AI Weather Quest contributors'
author = 'Joshua Talib'

release = '1.0'
version = '1.1.4'

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output

html_theme = 'sphinx_rtd_theme'
html_logo = os.path.abspath("acacia_logo.png")

# -- Options for EPUB output
epub_show_urls = 'footnote'
