# Dash Bootstrap Templates

`dash-bootstrap-templates` provides a collection of Plotly figure templates customized for Bootstrap themes. 
This library has a template for each of the 22 Bootstrap/Bootswatch themes available in the
[Dash Bootstrap Components Library](https://dash-bootstrap-components.opensource.faculty.ai/).

##  See a live demo at [Dash Bootstrap Theme Explorer](https://hellodash.pythonanywhere.com/dash_bootstrap_templates)
## Quickstart
```python"
pip install dash-bootstrap-templates
```

```python

import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import dash_bootstrap_components as dbc

from dash_bootstrap_templates import load_figure_template

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
load_figure_template("bootstrap")


df = px.data.gapminder().query("continent != 'Asia'")  # remove Asia for visibility
fig = px.line(df, x="year", y="lifeExp", color="continent", line_group="country")


app.layout = dbc.Container(
    [
        html.H1("Dash Bootstrap Template Demo", className="bg-primary text-white p-2"),
        dbc.Row(dbc.Col(dcc.Graph(figure=fig))),
    ],
    fluid=True,
)

if __name__ == "__main__":
    app.run_server(debug=True)
```
![image](https://user-images.githubusercontent.com/72614349/115889093-7c7a1000-a408-11eb-8bff-7773327016e8.png)




## Demo App 2 - 4 Graphs Updated

This demo [(code here)](https://github.com/AnnMarieW/dash-bootstrap-templates/blob/main/examples/demo_4_graphs.py),
shows how all 4 graphs are updated with one line of code.  Use `load_figure_template()` to load the Bootstrap themed 
figure template that matches the theme in the `external_style_sheets`.

![figure_template2](https://user-images.githubusercontent.com/72614349/129459807-30c22ffe-7a8c-44b9-9555-6cfd50ec355b.png)



## Demo App 3 - Theme Switcher

This demo [(code here)](https://github.com/AnnMarieW/dash-bootstrap-templates/blob/main/examples/theme_switcher.py),
shows an app with a toggle switch to change between two themes. The dash-bootstrap-templates library makes it easy to update all
the figures in the app when the theme changes with the toggle.  To see other CSS that may be necessary when switching themes see the 
Dash Bootstrap Theme Explorer App [live demo here.](https://hellodash.pythonanywhere.com/theme_explorer)

![theme_switch_toggle](https://user-images.githubusercontent.com/72614349/131913051-700ddad2-e3ae-4c6f-a6e8-f40f8fe845fb.gif)



## Background

[Dash Labs](https://community.plotly.com/t/introducing-dash-labs/52087) is a new Plotly library that explores cutting edge technology and extends what’s possible to do with Dash. 
One innovative experimental feature creates figure templates based on Bootstrap themes. Some Dash Labs layout templates are Bootstrap-themed.  Those can, at your option, generate figure templates at runtime.

`dash-bootstrap-templates` makes Dash Labs' figure templates available for any version of Dash. It uses Dash Labs' 
algorithms to generate the 22 most common Bootstrap figure
templates and saves them in json format.   `load_figure_template()` reads the json
file, adds it to `plotly.io` and sets it as the default figure template for an app.  See more 
information about  Plotly
figure templates [here](https://plotly.com/python/templates/).


## Available Themes

This library provis a figure template for the following Bootstrap/Bootswatch themes:

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

### Contributors
Special thanks to @tcbegley for [the pull request](https://github.com/AnnMarieW/dash-bootstrap-templates/pull/2) to
set up this library to publish to PyPI