from dash import Dash, dcc, html, Input, Output, dash_table, callback
import pandas as pd
import plotly.express as px
import dash_bootstrap_components as dbc
import dash_ag_grid as dag
import plotly.io as pio

from dash_bootstrap_templates import ThemeSwitchAIO

app = Dash(__name__)

##### Test dbc themes:
# themes = (dbc.themes.BOOTSTRAP, dbc.themes.CYBORG)

##### Test custom themes and do not apply automatically custom_color_mode_theme.css in assets for this example:
# themes = ("/assets/custom_light_theme.css", "/assets/custom_dark_theme.css")
# app.config.assets_ignore = 'custom_color_mode_theme.css'

##### Test color mode, provide only one url as a string:
themes = dbc.themes.SPACELAB

##### Test custom color mode and do not apply automatically custom_dark_theme.css
##### and custom_light_theme.css in assets for this example:
# themes = '/assets/custom_color_mode_theme.css'
# app.config.assets_ignore = 'custom_dark_theme.css|custom_light_theme.css'

df = pd.DataFrame(
    {
        "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
        "Amount": [4, 1, 2, 2, 4, 5],
        "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"],
    }
)

app.layout = [
    html.Div(
        [
            html.H3("ThemeSwitchAIO Demo"),
            dbc.Checkbox(id="alt-icons-chk", label="Use alternative switch icons"),
            ThemeSwitchAIO(aio_id="theme", themes=themes)
        ], className="sticky-top bg-secondary"
    ),
    html.H4('Dash Bootstrap Components:'),
    html.Div(
        [
            dbc.Button(f"{color}", color=f"{color}", size="sm")
            for color in ["primary", "secondary", "success", "warning", "danger", "info", "light", "dark", "link"]
        ]
    ),
    dbc.Checklist(['New York City', 'Montréal', 'San Francisco'], ['New York City', 'Montréal'], inline=True),
    dbc.RadioItems(['New York City', 'Montreal', 'San Francisco'], 'Montreal', inline=True),
    html.Hr(),
    html.H4('Dash Core Components:'),
    dcc.Checklist(['New York City', 'Montréal', 'San Francisco'], ['New York City', 'Montréal'], inline=True),
    dcc.RadioItems(['New York City', 'Montreal', 'San Francisco'], 'Montreal', inline=True),
    dcc.Dropdown(["Apple", "Carrots", "Chips", "Cookies"], ["Cookies", "Carrots"], multi=True),
    dcc.Slider(min=0, max=20, step=5, value=10),
    html.Hr(),
    html.H4('Dash DataTable:'),
    dash_table.DataTable(
        columns=[{"name": i, "id": i} for i in df.columns],
        data=df.to_dict("records"),
        row_selectable="single",
        row_deletable=True,
        editable=True,
        filter_action="native",
        sort_action="native",
        style_table={"overflowX": "auto"},
    ),
    html.Hr(),
    html.H4('Dash AG Grid:'),
    dag.AgGrid(
        columnDefs=[{"field": i} for i in df.columns],
        rowData=df.to_dict("records"),
        defaultColDef={
            "flex": 1, "filter": True,
            "checkboxSelection": {
                "function": 'params.column == params.api.getAllDisplayedColumns()[0]'
            },
            "headerCheckboxSelection": {
                "function": 'params.column == params.api.getAllDisplayedColumns()[0]'
            }
        },
        dashGridOptions={"rowSelection": "multiple", "domLayout": "autoHeight"},
        className='ag-theme-quartz'
    ),
    html.Hr(),
    html.H4('Plotly Figure:'),
    dcc.Graph(
        id='theme_switch-graph',
        figure=px.bar(df, x="Fruit", y="Amount", color="City", barmode="group")
    )
]


# Switch figure themes
@callback(
    Output("theme_switch-graph", "figure"),
    Input(ThemeSwitchAIO.ids.switch("theme"), "value"),
)
def update_figure_template(switch_on):
    return px.bar(
        df, x="Fruit", y="Amount", color="City", barmode="group",
        template=pio.templates["minty" if switch_on else "cyborg"]
    )


# Test changing the icons
@callback(
    Output(ThemeSwitchAIO.ids.leftIcon("theme"), "className"),
    Output(ThemeSwitchAIO.ids.rightIcon("theme"), "className"),
    Input("alt-icons-chk", "value"),
)
def use_alt_icons(alt_icons):
    return ("fa fa-bed", "fa fa-smile") if alt_icons else ("fa fa-moon", "fa fa-sun")


if __name__ == "__main__":
    app.run(debug=True)
