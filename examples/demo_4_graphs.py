"""
Apply Bootstrap theme to figures with one line of code! See more info at dash-bootstrap-templates GitHub
pip install dash-bootstrap-templates
"""

import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import dash_bootstrap_components as dbc

from dash_bootstrap_templates import load_figure_template

# This loads the "cyborg" themed figure template from dash-bootstrap-templates library,
# adds it to plotly.io and makes it the default figure template.
load_figure_template("cyborg")

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.CYBORG])

df = px.data.gapminder()

dff = df[df.year.between(1952, 1982)]
dff = dff[dff.continent.isin(df.continent.unique()[1:])]
line_fig = px.line(
    dff, x="year", y="gdpPercap", color="continent", line_group="country"
)

dff = dff[dff.year == 1982]
scatter_fig = px.scatter(
    dff, x="lifeExp", y="gdpPercap", size="pop", color="pop", size_max=60
).update_traces(marker_opacity=0.8)

avg_lifeExp = (dff["lifeExp"] * dff["pop"]).sum() / dff["pop"].sum()
map_fig = px.choropleth(
    dff,
    locations="iso_alpha",
    color="lifeExp",
    title="%.0f World Average Life Expectancy was %.1f years" % (1982, avg_lifeExp),
)

hist_fig = px.histogram(dff, x="lifeExp", nbins=10, title="Life Expectancy")

graphs = html.Div(
    [
        dbc.Row(
            [
                dbc.Col(dcc.Graph(figure=line_fig), lg=6),
                dbc.Col(dcc.Graph(figure=scatter_fig), lg=6),
            ],
            className="mt-4",
        ),
        dbc.Row(
            [
                dbc.Col(dcc.Graph(figure=hist_fig), lg=6),
                dbc.Col(dcc.Graph(figure=map_fig), lg=6),
            ],
            className="mt-4",
        ),
    ]
)

# These buttons are added to the app just to show the Boostrap theme colors
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
)

heading = html.H1("Dash Bootstrap Template Demo", className="bg-primary text-white p-2")

app.layout = dbc.Container(fluid=True, children=[heading, buttons, graphs])


if __name__ == "__main__":
    app.run_server(debug=True)