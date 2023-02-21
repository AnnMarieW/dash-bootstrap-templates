from dash import Dash, dcc, html
from dash_bootstrap_templates import ThemeSwitchAIO, ThemeChangerAIO
import dash_bootstrap_components as dbc

app = Dash(__name__)

app.layout = html.Div([ThemeSwitchAIO(aio_id='theme',
                                      themes=["/assets/testing_light.css", "/assets/testing_dark.css"]
                                      ), 'testing', dbc.Button()], id='testing')



if __name__ == "__main__":
    app.run(debug=True)