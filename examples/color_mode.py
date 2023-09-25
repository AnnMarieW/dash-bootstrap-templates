
"""
Example of light and dark color modes available in Bootstrap >= 5.3
"""
from dash import Dash, html, dcc, Input, Output, clientside_callback, callback
import plotly.express as px
import dash_bootstrap_components as dbc

from dash_bootstrap_templates import load_figure_template
load_figure_template(["minty", "minty_dark"])


df = px.data.gapminder()

app = Dash(__name__, external_stylesheets=[dbc.themes.MINTY, dbc.icons.FONT_AWESOME])

color_mode_switch =  html.Span(
    [
        dbc.Label(className="fa fa-moon", html_for="switch"),
        dbc.Switch( id="switch", value=True, className="d-inline-block ms-1", persistence=True),
        dbc.Label(className="fa fa-sun", html_for="switch"),
    ]
)

app.layout = dbc.Container(
    [
        html.Div(["Bootstrap Light Dark Color Modes Demo"], className="bg-primary text-white h3 p-2"),
        color_mode_switch,
        dcc.Graph(id="graph", className="border"),
    ]

)

@callback(
    Output("graph", "figure"),
    Input("switch", "value"),
)
def update_figure_template(switch_on):
    template = "minty" if switch_on else "minty_dark"
    fig = px.scatter(
        df.query("year==2007"),
        x="gdpPercap",
        y="lifeExp",
        size="pop",
        color="continent",
        log_x=True,
        size_max=60,
        template=template,
    )
    return fig



clientside_callback(
    """
    (switchOn) => {
       switchOn
         ? document.documentElement.setAttribute('data-bs-theme', 'light')
         : document.documentElement.setAttribute('data-bs-theme', 'dark')
       return window.dash_clientside.no_update
    }
    """,
    Output("switch", "id"),
    Input("switch", "value"),
)


if __name__ == "__main__":
    app.run_server(debug=True)
