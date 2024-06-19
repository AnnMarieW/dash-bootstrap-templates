import os

from .aio_theme_switch import ThemeSwitchAIO
from .aio_theme_changer import ThemeChangerAIO, template_from_url

# needed for Dash for _js_dist
from dash_bootstrap_templates import __version__

_js_dist = [
    {
        "namespace": "aio",
        "relative_package_path": "clientsideCallbacks.js",
        "external_url": f'{os.path.dirname(os.path.realpath(__file__))}\\clientsideCallbacks.js',
    }
]
