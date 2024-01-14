"""
A sample of 8 of the 26 Bootstrap themed Plotly figure templates available
in the dash-bootstrap-template library

"""
import dash
from dash import Dash, html, dcc, Input, Output, callback
import dash_bootstrap_components as dbc
from dash_bootstrap_templates import load_figure_template
import plotly.express as px


df = px.data.gapminder()

themes = [
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
    "morph",
    "quartz",
    "vapor",
    "zephyr",
]

dark_themes = [t+"_dark" for t in themes]
all_templates = themes + dark_themes
all_templates.sort()


load_figure_template("all")

figures = [
    px.scatter(
        df.query("year==2007"),
        x="gdpPercap",
        y="lifeExp",
        size="pop",
        color="continent",
        log_x=True,
        size_max=60,
        template=template,
        title="Gapminder 2007: '%s' theme" % template,
    )
    for template in all_templates
]

button = dbc.Button("Show all 52 Themes!", id="figure_templates_all-x-btn", n_clicks=0)

app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = dbc.Container(
        [button, dcc.Loading(html.Div(id="figure_templates_all-x-content", className="my-2"))]
)



@callback(
    Output("figure_templates_all-x-content", "children"),
    Input("figure_templates_all-x-btn", "n_clicks"),
    prevent_initial_call=True,
)
def update(n):
    if n > 0:
        return [dcc.Graph(figure=fig, className="m-4") for fig in figures]
    else:
        return dash.no_update


if __name__ == "__main__":
    app.run_server(debug=True)