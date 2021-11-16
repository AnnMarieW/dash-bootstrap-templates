"""
This is a minimal example of changing themes with the ThemeChangerAIO component
Note - this requires dash-bootstrap-components>=1.0.0 and dash>=2.0
    pip install dash-bootstrap-templates=1.0.0.

The ThemeChangerAIO component updates the Plotly default figure template when the
theme changes, but the figures must be updated in a callback in order to render with the new template.

This example demos:
 - how to update the figure for the new theme in a callback
 - using the dbc class which helps improve the style when the themes are switched. See the dbc.css file in the dash-bootstrap-templates library.
"""

from dash import Dash, dcc, html, Input, Output
import pandas as pd
import plotly.express as px
import dash_bootstrap_components as dbc
from dash_bootstrap_templates import ThemeChangerAIO, template_from_url

dbc_css = (
    "https://cdn.jsdelivr.net/gh/AnnMarieW/dash-bootstrap-templates@V1.0.1/dbc.min.css"
)
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP, dbc_css])


df = pd.DataFrame(
    {
        "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
        "Amount": [4, 1, 2, 2, 4, 5],
        "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"],
    }
)
header = html.H4(
    "ThemeChangerAIO Demo", className="bg-primary text-white p-4 mb-2 text-center"
)
buttons = html.Div(
    [
        dbc.Button("Primary", color="primary"),
        dbc.Button("Secondary", color="secondary"),
        dbc.Button("Success", color="success"),
        dbc.Button("Warning", color="warning"),
        dbc.Button("Danger", color="danger"),
        dbc.Button("Info", color="info"),
        dbc.Button("Light", color="light"),
        dbc.Button("Dark", color="dark"),
        dbc.Button("Link", color="link"),
    ],
    className="m-4",
)

graph = html.Div(dcc.Graph(id="graph"), className="m-4")

app.layout = dbc.Container(
    [
        header,
        dbc.Row(
            [
                dbc.Col(
                    ThemeChangerAIO(
                        aio_id="theme", radio_props={"value": dbc.themes.FLATLY}
                    ),
                    width=2,
                ),
                dbc.Col([buttons, graph], width=10),
            ]
        ),
    ],
    className="m-4 dbc",
    fluid=True,
)


@app.callback(
    Output("graph", "figure"), Input(ThemeChangerAIO.ids.radio("theme"), "value"),
)
def update_graph_theme(theme):
    return px.bar(
        df,
        x="Fruit",
        y="Amount",
        color="City",
        barmode="group",
        template=template_from_url(theme),
    )


if __name__ == "__main__":
    app.run_server(debug=True)
