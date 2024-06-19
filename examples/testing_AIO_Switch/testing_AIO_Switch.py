from dash import Dash, dcc, html
from dash_bootstrap_templates import ThemeSwitchAIO, ThemeChangerAIO
import dash_bootstrap_components as dbc

dbc_css = (
    "https://cdn.jsdelivr.net/gh/AnnMarieW/dash-bootstrap-templates@V1.0.1/dbc.min.css"
)
app = Dash(__name__, external_stylesheets=[dbc_css])

app.layout = html.Div(
    [
        ThemeSwitchAIO(
            aio_id='theme',
            # themes=["/assets/testing_light.css", "/assets/testing_dark.css"]
        ),
        'testing',
        dbc.Button()
    ], id='testing'
)

if __name__ == "__main__":
    app.run(debug=True)
