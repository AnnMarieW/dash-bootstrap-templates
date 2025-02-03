"""
This is a demo of the `vizro.bootstrap` theme combined with the load_figure_template(themes) function
from dash_bootstrap_templates.py

Unlike other Bootstrap themes, the `vizro.bootstrap` theme is not included in the `dbc.themes` module and
must be imported from the `vizro` module.

The `load_figure_template` function behaves as expected: it loads the Bootstrap theme, adds it to `plotly.io`,
and sets it as the default.
"""

from dash import Dash, dcc, html
import plotly.express as px
import dash_bootstrap_components as dbc
import vizro

from dash_bootstrap_templates import load_figure_template

app = Dash(__name__, external_stylesheets=[vizro.bootstrap])
load_figure_template("vizro")


df = px.data.gapminder().query("continent != 'Asia'")  # remove Asia for visibility
fig = px.line(df, x="year", y="lifeExp", color="continent", line_group="country")


app.layout = dbc.Container(
    [
        html.H1("Vizro Bootstrap Template Demo", className="bg-primary p-2"),
        dbc.Row(dbc.Col(dcc.Graph(figure=fig))),
    ],
    fluid=True,
)


if __name__ == "__main__":
    app.run_server(debug=True)
