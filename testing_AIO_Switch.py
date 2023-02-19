from dash import Dash, dcc, html
from src.aio.aio_theme_switch import ThemeSwitchAIO
import dash_bootstrap_components as dbc

app = Dash(__name__)

app.layout = html.Div([ThemeSwitchAIO(aio_id='theme'), 'testing', dbc.Button()], id='testing')

app.run(debug=True)