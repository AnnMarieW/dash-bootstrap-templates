# Dash Bootstrap Templates

Dash Bootstrap Templates a collection of Plotly figure templates that
are customized for Bootstrap themes.

There are templates for each of the 22 themes available in the [Dash Bootstrap
Components Library](https://dash-bootstrap-components.opensource.faculty.ai/)


## Quickstart

`pip install dash-bootstrap-templates`

This example loads the Minty figure template:

```
from dash_bootstrap_templates import load_figure_template
load_figure_template("minty")
```
Here are 3 demo apps:

demo_minty.py

demo_sketchy.py

demo_superhero.py




## Background

One of the nice features in [Dash Labs]() is the Bootstrap figure templates.  As you can see
in the demo apps, it makes it effortless to create graphs with a style that's consistent with
your selected Bootstrap theme.

In Dash Labs, these templates are created on-the-fly by setting figure_template=True, 
in certain layout templates.   This library makes these figure templates available for use
in a Dash app the same way as any other build-in Plotly figure templated.   It does this by
using the Dash Labs algorithms to generate the 22 most common Bootstrap figure
templates and saves them in a json format.   The load_figure_template() function reads the json
file, adds it to plotly.io and sets it as the default template for an app.

Here are the advantages of this method rather than creating the templates on-the-fly:

- It makes these templates available for use in any app using Dash or any of the Dash Labs layout
  templates. Currently, these are available only in a few of the Dash Labs layout templates.
-  Since the templates are not create on-the-fly, it increases app performance and 
   eliminates the risk that the template fail to build.
-  The runtime dependency of tinycss2 and spectra in Dash Labs is eliminated.

## Available Themes

This library has figure templates for the following Bootstrap/Bootswatch themes:

valid_themes = [
    "bootstrap",
    "cerulean",
    "cosmo",
    "flatly",
    "journal",
    "litera",
    "lumen",
    "lux",
    "materia",
    "minty",
    "pulse",
    "sandstone",
    "simplex",
    "sketchy",
    "spacelab",
    "united",
    "yeti",
    "cyborg",
    "darkly",
    "slate",
    "solar",
    "superhero",
]
