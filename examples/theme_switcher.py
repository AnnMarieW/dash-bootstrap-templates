"""
This is a minimal example of a theme switcher clientside callback with a toggle switch.

The Bootstrap themed templates are from the dash-bootstrap-templates library.
See more information at https://github.com/AnnMarieW/dash-bootstrap-templates
    pip install dash-bootstrap-templates.
"""

import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output
import pandas as pd
import plotly.express as px

import dash_bootstrap_components as dbc
from dash_bootstrap_templates import load_figure_template

# This adds the "bootstrap" and "cyborg" themed templates  to the Plolty figure templates
load_figure_template(["bootstrap", "cyborg"])

FONT_AWESOME = "https://use.fontawesome.com/releases/v5.10.2/css/all.css"
app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP, FONT_AWESOME])

df = pd.DataFrame(
    {
        "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
        "Amount": [4, 1, 2, 2, 4, 5],
        "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"],
    }
)

toggle = html.Div(
    [
        html.Span(className="fa fa-moon"),
        dbc.Checklist(
            options=[{"value": 1}],
            value=[1],
            id="theme",
            switch=True,
            className="d-inline-block ml-2",
            inputStyle={"height": 30, "width": 30},
        ),
        html.Span(className="fa fa-sun"),
    ],
    className="d-inline-block",
)

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

# dummy output needed by the clientside callback
blank = html.Div(id="blank_output")

"""
===============================================================================
Layout
"""
app.layout = dbc.Container(
    dbc.Row([dbc.Col([toggle, buttons, graph, blank])]), className="m-4", fluid=True,
)


@app.callback(
    Output("graph", "figure"), Input("theme", "value"),
)
def update_graph_theme(value):
    template = "bootstrap" if value == [1] else "cyborg"
    return px.bar(
        df, x="Fruit", y="Amount", color="City", barmode="group", template=template
    )


app.clientside_callback(
    """
    function(theme) {
        //  To use different themes,  change these links:
        const theme1 = "https://stackpath.bootstrapcdn.com/bootstrap/4.5.0/css/bootstrap.min.css"
        const theme2 = "https://stackpath.bootstrapcdn.com/bootswatch/4.5.0/cyborg/bootstrap.min.css"

        const stylesheet = document.querySelector('link[rel=stylesheet][href^="https://stackpath"]')        
        var themeLink = (theme.length == 1) ? theme1 : theme2;
        stylesheet.href = themeLink
    }
    """,
    Output("blank_output", "children"),
    Input("theme", "value"),
)

if __name__ == "__main__":
    app.run_server(debug=True)