"""
This is a minimal example of a theme switcher clientside callback with a toggle switch.
Note - this is the version for dash-bootstrap-components V1.0.  and Dash V2.0
See more information at https://github.com/AnnMarieW/dash-bootstrap-templates
    pip install dash-bootstrap-templates=1.0.0.

The ThemeSwitchAIO component updates the Plotly default figure template when the
theme changes, but the figures must be updated in a callback in order to render with the new template.
See the callback below for an example.

"""

from dash import Dash, dcc, html, Input, Output
import pandas as pd
import plotly.express as px
import dash_bootstrap_components as dbc
from dash_bootstrap_templates import ThemeSwitchAIO

# select the Bootstrap stylesheet2 and figure template2 for the theme toggle here:
template_theme1 = "sketchy"
template_theme2 = "darkly"
url_theme1 = dbc.themes.SKETCHY
url_theme2 = dbc.themes.DARKLY

app = Dash(__name__, external_stylesheets=[url_theme1])

df = pd.DataFrame(
    {
        "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
        "Amount": [4, 1, 2, 2, 4, 5],
        "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"],
    }
)
header = html.H4("ThemeSwitchAIO Demo", className="bg-primary text-white p-4 mb-2")
buttons = html.Div(
    [
        dbc.Button("Primary", color="primary", className="mr-1"),
        dbc.Button("Secondary", color="secondary", className="mr-1"),
        dbc.Button("Success", color="success", className="mr-1"),
        dbc.Button("Warning", color="warning", className="mr-1"),
        dbc.Button("Danger", color="danger", className="mr-1"),
        dbc.Button("Info", color="info", className="mr-1"),
        dbc.Button("Light", color="light", className="mr-1"),
        dbc.Button("Dark", color="dark", className="mr-1"),
        dbc.Button("Link", color="link"),
    ],
    className="m-4",
)
graph = html.Div(dcc.Graph(id="graph"), className="m-4")

"""
===============================================================================
Layout
"""
app.layout = dbc.Container(
    dbc.Row(
        [
            dbc.Col(
                [
                    header,
                    ThemeSwitchAIO(
                        aio_id="theme",
                        themes=[url_theme1, url_theme2],
                    ),
                    buttons,
                    graph,
                ]
            )
        ]
    ),
    className="m-4",
    fluid=True,
)


@app.callback(
    Output("graph", "figure"), Input(ThemeSwitchAIO.ids.switch("theme"), "value"),
)
def update_graph_theme(toggle):
    template = template_theme1 if toggle else template_theme2
    return px.bar(df, x="Fruit", y="Amount", color="City", barmode="group", template=template)


if __name__ == "__main__":
    app.run_server(debug=True)
