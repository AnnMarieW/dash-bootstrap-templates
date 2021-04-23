"""
Use this function to make the bootstrap figure templates available in your Dash app

"""


def load_figure_template(themes='bootstrap'):
    """Add figure template to plotly.io and sets the default template

        Keyword arguments:
        themes -- may be a string or list of strings. (Default "bootstrap")
                  The string is the lowercase name of a Bootstrap theme
                  built in _create_templates.py

        The plotly.io.templates.default will be the first theme if
        themes is a list. If the themes attribute is invalid, the
        "bootstrap" theme will be used.
        """

    import json
    import pathlib
    import plotly.io as pio

    # set relative path
    PATH = pathlib.Path(__file__).parent
    TEMPLATES_PATH = PATH.joinpath("./templates").resolve()

    def read_template(theme):
        try:
            with open(TEMPLATES_PATH.joinpath(f"{theme}.json"), "r") as f:
                template = json.load(f)
        except IOError:
            with open(TEMPLATES_PATH.joinpath("bootstrap.json"), "r") as f:
                template = json.load(f)
        pio.templates[theme] = template

    if type(themes) is list:
        for theme in themes:
            read_template(theme)
        pio.templates.default = themes[0]

    else:
        read_template(themes)
        pio.templates.default = themes
