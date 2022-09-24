from dash import Dash, dcc, html, Input, Output
import plotly.express as px
import dash_bootstrap_components as dbc
from dash_bootstrap_templates import ThemeChangerAIO, template_from_url

dbc_css = (
    "https://cdn.jsdelivr.net/gh/AnnMarieW/dash-bootstrap-templates@V1.0.1/dbc.min.css"
)

app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP, dbc_css])

iris = px.data.iris()
gapminder = px.data.gapminder()
tips = px.data.tips()
carshare = px.data.carshare()

figure_templates = [
    "bootstrap_theme",
    "plotly",
    "ggplot2",
    "seaborn",
    "simple_white",
    "plotly_white",
    "plotly_dark",
    "presentation",
    "xgridoff",
    "ygridoff",
    "gridon",
    "none",
]

change_theme = ThemeChangerAIO(
    aio_id="theme",
    radio_props={"value": dbc.themes.SUPERHERO},
    button_props={
        "size": "lg",
        "outline": False,
        "style": {"marginTop": ".5rem"},
        "color": "success",
    },
)

change_figure_template = html.Div(
    [
        html.Div("Change Figure Template"),
        dcc.Dropdown(figure_templates, "bootstrap_theme", id="template"),
    ],
    className="pb-4",
)

sources = html.Div(
    [
        html.P("By Tuomas Poukkula"),
        html.Label(
            [
                "Sources: ",
                html.A(
                    "Dash Bootstrap Templates| ",
                    href="https://pypi.org/project/dash-bootstrap-templates/0.1.1/",
                    target="_blank",
                ),
                html.A(
                    "Plotly Templates| ",
                    href="https://plotly.com/python/templates/",
                    target="_blank",
                ),
                html.A(
                    "Plotly Express",
                    href="https://plotly.com/python/plotly-express/",
                    target="_blank",
                ),
            ]
        ),
    ]
)


def make_figures(template):
    graph1 = dcc.Graph(
        figure=px.scatter(
            iris,
            x="sepal_width",
            y="sepal_length",
            color="species",
            title=f"Iris <br>{template} figure template",
            template=template,
        ),
        className="border",
    )
    print(graph1)
    graph2 = dcc.Graph(
        figure=px.scatter(
            gapminder,
            x="gdpPercap",
            y="lifeExp",
            size="pop",
            color="continent",
            hover_name="country",
            animation_frame="year",
            animation_group="country",
            log_x=True,
            size_max=60,
            title=f"Gapminder <br>{template} figure template",
            template=template,
        ),
        className="border",
    )
    graph3 = dcc.Graph(
        figure=px.violin(
            tips,
            y="tip",
            x="smoker",
            color="sex",
            box=True,
            points="all",
            hover_data=tips.columns,
            title=f"Tips <br>{template} figure template",
            template=template,
        ),
        className="border",
    )
    graph4 = dcc.Graph(
        figure=px.scatter_mapbox(
            carshare,
            lat="centroid_lat",
            lon="centroid_lon",
            color="peak_hour",
            size="car_hours",
            size_max=15,
            zoom=10,
            mapbox_style="carto-positron",
            title=f"Carshare <br> {template} figure template",
            template=template,
        ),
        className="border",
    )

    return [
        dbc.Row([dbc.Col(graph1, lg=6), dbc.Col(graph2, lg=6)]),
        dbc.Row([dbc.Col(graph3, lg=6), dbc.Col(graph4, lg=6)], className="mt-4"),
    ]


app.layout = dbc.Container(
    [
        dbc.Row(
            [
                dbc.Col(change_theme, lg=2),
                dbc.Col(change_figure_template, lg=4),
            ],
        ),
        dbc.Row(dbc.Col(html.Div(id="graphs"))),
        dbc.Row(dbc.Col(sources)),
    ],
    className="dbc p-4",
    fluid=True,
)


@app.callback(
    Output("graphs", "children"),
    Input(ThemeChangerAIO.ids.radio("theme"), "value"),
    Input("template", "value"),
)
def update_graph_theme(theme, template):
    template = template_from_url(theme) if template == "bootstrap_theme" else template

    return make_figures(template)


if __name__ == "__main__":
    app.run_server(debug=True)