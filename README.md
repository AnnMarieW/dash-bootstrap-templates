# Dash Bootstrap Templates

`dash-bootstrap-templates` provides a collection of Plotly figure templates customized for Bootstrap themes. 
This library has a template for each of the 22 Bootstrap/Bootswatch themes available in the
[Dash Bootstrap Components Library](https://dash-bootstrap-components.opensource.faculty.ai/).

## Quickstart

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




## Demo Apps

In the three demo apps below [(code here)](https://github.com/AnnMarieW/dash-bootstrap-templates/blob/main/demo_app.py),
each graph on the left uses a Bootstrap figure template.  The corresponding graph on the right uses the  `'plotly'` 
default figure template. Note that Bootstrap figure templates have colorways and fonts consistent
with the app's Bootstrap theme.



### Dash Bootstrap Template Compared To Plotly Default Template

### Minty
![image](https://user-images.githubusercontent.com/72614349/115973397-82a3e580-a509-11eb-8145-21907353248d.png)
---
---

### Superhero
![image](https://user-images.githubusercontent.com/72614349/115973461-01008780-a50a-11eb-8435-a9824fe7ce50.png)

---
---
### Cyborg
![image](https://user-images.githubusercontent.com/72614349/115973437-ce568f00-a509-11eb-8086-5570479be7ef.png)


## Background

[Dash Labs](https://community.plotly.com/t/introducing-dash-labs/52087) is a new library that explores cutting edge technology and extends what’s possible to do with Dash. 
One innovative new feature creates figure templates based on Bootstrap themes. Some Dash Labs layout templates are Bootstrap-themed.  Those can, at your option, generate figure templates at runtime.

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
