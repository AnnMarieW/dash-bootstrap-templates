from dash import Dash, dcc, html, Input, Output
import pandas as pd
import plotly.express as px
import dash_bootstrap_components as dbc
from dash_bootstrap_templates import ThemeSwitchAIO

"""
 
 Note!! - As of Dash Bootstrap Components V1.5.0, we recommend using the Bootstrap Light Dark Color Modes feature 
 to switch between light and dark versions of a single theme rather than using the ThemeSwitchAIO component.

For more info see https://hellodash.pythonanywhere.com/adding-themes/theme-switch

This example is for dbc <1.5.0

-------------------

Here is how you can download the Bootstrap stylesheets and place them in the assets folder so you can use the
theme switch component off-line.


print("theme1", dbc.themes.SKETCHY)
print("theme2", dbc.themes.DARKLY)

results in:
> theme1 https://cdn.jsdelivr.net/npm/bootswatch@5.3.1/dist/sketchy/bootstrap.min.css
> theme2 https://cdn.jsdelivr.net/npm/bootswatch@5.3.1/dist/darkly/bootstrap.min.css

You can open the link and save the content to files in the assets folder

"""


# figure templates
template_theme1 = "sketchy"
template_theme2 = "darkly"

dbc_css = "https://cdn.jsdelivr.net/gh/AnnMarieW/dash-bootstrap-templates/dbc.min.css"
#  Note that there are no external stylesheet added here:
app = Dash(__name__)

df = pd.DataFrame(
    {
        "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
        "Amount": [4, 1, 2, 2, 4, 5],
        "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"],
    }
)
header = html.H4("ThemeSwitchAIO Demo", className="bg-primary text-white p-4 mb-2")

theme_switch = ThemeSwitchAIO(aio_id="theme", themes=["/assets/theme1.css", "/assets/theme2.css" ])

theme_colors = [
    "primary",
    "secondary",
    "success",
    "warning",
    "danger",
    "info",
    "light",
    "dark",
    "link",
]
buttons = html.Div(
    [dbc.Button(f"{color}", color=f"{color}", size="sm") for color in theme_colors]
)
colors = html.Div(["Theme Colors:", buttons], className="mt-2")

graph = html.Div(dcc.Graph(id="theme_switch-x-graph"), className="m-4")


app.layout = dbc.Container(
    dbc.Row(dbc.Col([header, theme_switch, colors, graph])),
    className="m-4 dbc",
    fluid=True,
)


@app.callback(
    Output("theme_switch-x-graph", "figure"),
    Input(ThemeSwitchAIO.ids.switch("theme"), "value"),
)
def update_graph_theme(toggle):
    template = template_theme1 if toggle else template_theme2
    return px.bar(
        df, x="Fruit", y="Amount", color="City", barmode="group", template=template
    )


if __name__ == "__main__":
    app.run_server(debug=True)