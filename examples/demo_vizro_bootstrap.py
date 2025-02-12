"""
This script demonstrates the use of the `vizro.bootstrap` theme in combination with the `load_figure_template(themes)`
function from the `dash_bootstrap_templates.py` module.

Unlike other Bootstrap themes, the `vizro.bootstrap` theme is not included in the `dbc.themes` module. Therefore, you
need to import it directly from the `vizro` module. You can then add it to the external stylesheets of your Dash app:

```python
pip install vizro>=0.1.34

import vizro
from dash import Dash

app = Dash(__name__, external_stylesheets=[vizro.bootstrap])
```

In case you want to use the Vizro bootstrap theme without having to import vizro, you can also get the
latest CSS file via:

```python
vizro_bootstrap = "https://cdn.jsdelivr.net/gh/mckinsey/vizro@main/vizro-core/src/vizro/static/css/vizro-bootstrap.min.css"
app = Dash(__name__, external_stylesheets=[vizro_bootstrap])
```
"""
from dash import Dash, html, dcc, Input, Output, Patch, clientside_callback, callback
import plotly.express as px
import plotly.io as pio
import dash_bootstrap_components as dbc
# You need to install vizro>=0.1.34
import vizro

from dash_bootstrap_templates import load_figure_template

# Load data and figure templates
gapminder = px.data.gapminder().query("year==2007")
load_figure_template(["vizro", "vizro_dark"])

# Initialize the Dash app
app = Dash(__name__, external_stylesheets=[vizro.bootstrap, dbc.icons.FONT_AWESOME])

# Alternatively, you could do:
# vizro_bootstrap = "https://cdn.jsdelivr.net/gh/mckinsey/vizro@main/vizro-core/src/vizro/static/css/vizro-bootstrap.min.css"
# app = Dash(__name__, external_stylesheets=[vizro_bootstrap, dbc.icons.FONT_AWESOME])

# Create components for the dashboard
color_mode_switch = html.Span(
    [
        dbc.Label(className="fa fa-moon", html_for="switch"),
        dbc.Switch(id="switch", value=False, className="d-inline-block ms-1"),
        dbc.Label(className="fa fa-sun", html_for="switch"),
    ]
)
scatter = dcc.Graph(
    id="scatter", figure=px.scatter(gapminder, x="gdpPercap", y="lifeExp", size="pop", size_max=60, color="continent")
)
box = dcc.Graph(id="box", figure=px.box(gapminder, x="continent", y="lifeExp", color="continent"))


tabs = dbc.Tabs(
    [
        dbc.Tab(scatter, label="Scatter Plot"),
        dbc.Tab(box, label="Box Plot"),
    ]
)

# Create app layout
app.layout = dbc.Container(
    [html.H1("Vizro Bootstrap Demo", className="bg-primary p-2 mt-4"), color_mode_switch, tabs],
    fluid=True,
)


# Add callbacks to switch between dark / light
@callback(
    [Output("scatter", "figure"), Output("box", "figure")],
    Input("switch", "value"),
)
def update_figure_template(switch_on):
    """Sync the figure template with the color mode switch on the bootstrap template."""
    template = pio.templates["vizro"] if switch_on else pio.templates["vizro_dark"]
    patched_figure = Patch()
    patched_figure["layout"]["template"] = template

    return patched_figure, patched_figure


clientside_callback(
    """
    (switchOn) => {
       switchOn
         ? document.documentElement.setAttribute('data-bs-theme', 'light')
         : document.documentElement.setAttribute('data-bs-theme', 'dark')
       return window.dash_clientside.no_update
    }
    """,
    Output("switch", "id"),
    Input("switch", "value"),
)


if __name__ == "__main__":
    app.run(debug=True)
