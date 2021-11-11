import json

import plotly.io as pio

try:
    from importlib.resources import files
except ImportError:
    # if using Python 3.8 or lower import from the backport
    from importlib_resources import files

try:
    from importlib.metadata import (
        PackageNotFoundError,
        version,
    )
except ModuleNotFoundError:
    # if using Python 3.7, import from the backport
    from importlib_metadata import (
        PackageNotFoundError,
        version,
    )

try:
    __version__ = version("dash_bootstrap_templates")
except PackageNotFoundError:
    # package is not installed
    pass
"""
Use this function to make the bootstrap figure templates available in your Dash app
"""


def read_template(theme):
    try:
        with (
            files("dash_bootstrap_templates") / "templates" / f"{theme}.json"
        ).open() as f:
            template = json.load(f)
    except IOError:
        with (
            files("dash_bootstrap_templates") / "templates" / "bootstrap.json"
        ).open() as f:
            template = json.load(f)
    pio.templates[theme] = template


def load_figure_template(themes="bootstrap"):
    """Add figure template to plotly.io and sets the default template

    Keyword arguments:
    themes -- may be a string or list of strings. (Default "bootstrap")
              The string is the lowercase name of a Bootstrap theme
              built in _create_templates.py

    The plotly.io.templates.default will be the first theme if
    themes is a list. If the themes attribute is invalid, the
    "bootstrap" theme will be used.
    """
    if type(themes) is list:
        for theme in themes:
            read_template(theme)
        pio.templates.default = themes[0]

    else:
        read_template(themes)
        pio.templates.default = themes

from aio.aio_theme_changer import ThemeChangerAIO, template_from_url
from aio.aio_theme_switch import ThemeSwitchAIO