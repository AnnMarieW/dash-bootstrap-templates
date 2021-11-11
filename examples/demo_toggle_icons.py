"""
This is a minimal example of a theme switcher clientside callback with a toggle switch.
Note - this is the version for dash-bootstrap-components V1.0.  and Dash V2.0
See more information at https://github.com/AnnMarieW/dash-bootstrap-templates
    pip install dash-bootstrap-templates=1.0.0.

The ThemeSwitchAIO component updates the Plotly default figure template when the
theme changes, but the figures must be updated in a callback in order to render with the new template.
See the callback below for an example.

This example shows how to use different icons to the left and right of the toggle switch.
The default stylesheet for the icons is dbc.icons.FONTAWSOME, but you can use any icon stylesheet.  This example
uses the Boostrap icons.
"""

from dash import Dash, dcc, html, Input, Output
import pandas as pd
import plotly.express as px
import dash_bootstrap_components as dbc
from aio import ThemeSwitchAIO

# select the Bootstrap stylesheet2 and figure template2 for the theme toggle here:

template_theme1 = "quartz"
template_theme2 = "vapor"
url_theme1 = dbc.themes.QUARTZ
url_theme2 = dbc.themes.VAPOR

# note: using two themes stylesheets reduces the flicker when the theme changes.
#       This also loads the Bootstrap icons.
app = Dash(__name__, external_stylesheets=[url_theme1, dbc.icons.BOOTSTRAP])

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
                        icons={"left":"bi bi-moon", "right":"bi bi-sun"},
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
