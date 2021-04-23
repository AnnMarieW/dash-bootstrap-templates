#
"""
This is a demo of the `load_figure_template(themes)` function from dash_bootstrap_templates.py
It loads the Bootstrap theme template, adds it to plotly.io and makes it the default.

The app shows two graphs, the Bootstrap theme template vs the built-in default 'plotly' template

"""

from dash_bootstrap_templates import load_figure_template

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px
import dash_bootstrap_components as dbc


# Change the stylesheet and figure template here:
theme = "minty"
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.MINTY])
load_figure_template("minty")
#
# theme='sketchy'
# app = dash.Dash(__name__, external_stylesheets=[dbc.themes.SKETCHY])
# load_figure_template("sketchy")
#
# theme='superhero'
# app = dash.Dash(__name__, external_stylesheets=[dbc.themes.SUPERHERO])
# load_figure_template("superhero")


df = px.data.gapminder()

dropdown = dcc.Dropdown(
    id="indicator",
    options=[{"label": str(i), "value": i} for i in ["gdpPercap", "lifeExp", "pop"]],
    value="gdpPercap",
    clearable=False,
)


checklist = dbc.Checklist(
    id="continents",
    options=[{"label": i, "value": i} for i in df.continent.unique()],
    value=df.continent.unique()[3:],
    inline=True,
)

years = df.year.unique()
range_slider = dcc.RangeSlider(
    id="slider_years",
    min=years[0],
    max=years[-1],
    step=5,
    marks={int(i): str(i) for i in years},
    value=[1982, years[-1]],
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
    ]
)


controls = dbc.Card(
    [
        dbc.Row(
            [
                dbc.Col(
                    dbc.FormGroup([dbc.Label("Select indicator (y-axis)"), dropdown])
                ),
                dbc.Col(dbc.FormGroup([dbc.Label("Select continents"), checklist,])),
            ]
        ),
        dbc.FormGroup([dbc.Label("Select years"), range_slider, buttons,]),
    ],
    className="m-4 px-2",
)

app.layout = dbc.Container(
    [
        html.H1("Dash Bootstrap Template Demo", className="bg-primary text-white p-2"),
        dbc.Row(
            [
                dbc.Col(dcc.Graph(id="line_chart1"), lg=6),
                dbc.Col(dcc.Graph(id="line_chart2"), lg=6),
            ]
        ),
        controls,
        html.Hr(),
    ],
    id="layout_container",
    fluid=True,
)


@app.callback(
    Output("line_chart1", "figure"),
    Output("line_chart2", "figure"),
    Input("indicator", "value"),
    Input("continents", "value"),
    Input("slider_years", "value"),
)
def update_charts(indicator, continents, years):
    if continents == [] or indicator is None:
        return {}, {}

    dff = df[df.year.between(years[0], years[1])]
    fig1 = px.line(
        dff[dff.continent.isin(continents)],
        x="year",
        y=indicator,
        color="country",
        title=f"template='{theme}'",
    )

    fig2 = px.line(
        dff[dff.continent.isin(continents)],
        x="year",
        y=indicator,
        color="country",
        template="plotly",
        title="template='plotly'",
    )
    return fig1, fig2


if __name__ == "__main__":
    app.run_server(debug=True)


"""
Note:  For dark themed apps, add the following the css file in the assets folder.  This 
       styles the dropdown menu items to make them visible in both light and dark theme apps.
       See more info here: https://dash.plotly.com/external-resources


.VirtualizedSelectOption {
    background-color: white;
    color: black;
}

.VirtualizedSelectFocusedOption {
    background-color: lightgrey;
    color: black;
}

"""
