#
"""
This is a demo of the `load_figure_template(themes)` function from dash_bootstrap_templates.py
It loads the Bootstrap theme template, adds it to plotly.io and makes it the default.

The app shows two graphs, the Bootstrap theme template vs the built-in default 'plotly' template

"""

from dash_bootstrap_templates import load_figure_template

from dash import Dash, dcc, html, Input, Output
import plotly.express as px
import dash_bootstrap_components as dbc

# select the Bootstrap stylesheet and figure template for the theme here:
template_theme = "vapor"
url_theme = dbc.themes.VAPOR
# -----------------------------

app = Dash(__name__, external_stylesheets=[url_theme])
load_figure_template(template_theme)


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
    value=df.continent.unique()[1:],
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
        dbc.Button("Primary", color="primary"),
        dbc.Button("Secondary", color="secondary"),
        dbc.Button("Success", color="success"),
        dbc.Button("Warning", color="warning"),
        dbc.Button("Danger", color="danger"),
        dbc.Button("Info", color="info"),
        dbc.Button("Light", color="light"),
        dbc.Button("Dark", color="dark"),
        dbc.Button("Link", color="link"),
    ]
)


controls = dbc.Card(
    [
        dbc.Row(
            [
                dbc.Col([dbc.Label("Select indicator (y-axis)"), dropdown]),
                dbc.Col([dbc.Label("Select continents"), checklist,]),
            ]
        ),
        dbc.Row([dbc.Label("Select years"), range_slider, buttons,]),
    ],
    className="m-4 px-2",
)

app.layout = dbc.Container(
    [
        html.H1(
            "Dash Bootstrap Template vs Plolty Default Template",
            className="bg-primary text-white p-2",
        ),
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
    className="dbc",
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
    dff = dff[dff.continent.isin(continents)]
    fig1 = px.line(
        dff,
        x="year",
        y=indicator,
        color="continent",
        line_group="country",
        title=f"template='{template_theme}'",
    )

    fig2 = px.line(
        dff,
        x="year",
        y=indicator,
        color="continent",
        line_group="country",
        template="plotly",
        title="template='plotly'",
    )
    return fig1, fig2


if __name__ == "__main__":
    app.run_server(debug=True)
