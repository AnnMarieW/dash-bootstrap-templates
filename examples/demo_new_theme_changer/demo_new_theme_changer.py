from dash import Dash, dcc, html, Input, Output, dash_table, callback
import pandas as pd
import plotly.express as px
import dash_bootstrap_components as dbc
import dash_ag_grid as dag

from dash_bootstrap_templates import ThemeChangerAIO, template_from_url

app = Dash(
    __name__,
    external_stylesheets=["https://cdn.jsdelivr.net/gh/AnnMarieW/dash-bootstrap-templates/dbc.min.css"],
    ########## test custom server/client assets folders ##########
    assets_folder='server_side_assets',
    assets_url_path='client_side_assets'
)

df = pd.DataFrame({
    "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
    "Amount": [4, 1, 2, 2, 4, 5],
    "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"],
})

app.layout = html.Div(
    [
        # header
        html.Div(
            [
                html.H3("ThemeChangerAIO Demo"),
                ThemeChangerAIO(
                    aio_id="theme",
                    button_props={'outline': False},
                    ########## test custom themes ##########
                    custom_themes={
                        'custom-light': 'custom_light_theme.css',
                        'custom-dark': 'custom_dark_theme.css'
                    },
                    custom_dark_themes=['custom-dark'],
                    ########## test custom RadioItems list ##########
                    ## Note: the value must match the name of the theme
                    # radio_props={
                    #     "options": [
                    #         {"label": "Cyborg", "value": dbc.themes.CYBORG},
                    #         {"label": "My Theme", "value": "custom_light_theme.css"},
                    #         {"label": "My Dark Theme", "value": "custom_dark_theme.css"},
                    #         {"label": "Spacelab", "value": dbc.themes.SPACELAB},
                    #         # test setting label styling (here unset the style)
                    #         {"label": "Vapor", "value": dbc.themes.VAPOR, "label_id": ""}
                    #     ],
                    #     "value": dbc.themes.VAPOR,
                    # },
                    ########## test persistence ##########
                    # radio_props={"persistence": True},
                ),
            ], className="sticky-top bg-primary p-2"
        ),

        # test DBC components
        html.H4('Dash Bootstrap Components:'),
        html.Div([
            dbc.Button(f"{color}", color=f"{color}", size="sm")
            for color in ["primary", "secondary", "success", "warning", "danger", "info", "light", "dark", "link"]
        ]),
        dbc.Checklist(['New York City', 'Montréal', 'San Francisco'], ['New York City', 'Montréal'], inline=True),
        dbc.RadioItems(['New York City', 'Montreal', 'San Francisco'], 'Montreal', inline=True),
        html.Hr(),

        # test DCC components
        html.H4('Dash Core Components:'),
        dcc.Checklist(['New York City', 'Montréal', 'San Francisco'], ['New York City', 'Montréal'], inline=True),
        dcc.RadioItems(['New York City', 'Montreal', 'San Francisco'], 'Montreal', inline=True),
        dcc.Dropdown(["Apple", "Carrots", "Chips", "Cookies"], ["Cookies", "Carrots"], multi=True),
        dcc.Slider(min=0, max=20, step=5, value=10),
        html.Hr(),

        # test DataTable
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

        # test DAG
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
            className='ag-theme-quartz dbc-ag-grid'
        ),
        html.Hr(),

        # test plotly fig
        html.H4('Plotly Figure:'),
        dcc.Graph(
            id='theme_changer-graph',
            figure=px.bar(df, x="Fruit", y="Amount", color="City", barmode="group")
        )
    ], className='dbc'
)


# Switch figure themes
@callback(
    Output("theme_changer-graph", "figure"),
    Input(ThemeChangerAIO.ids.radio("theme"), "value"),
)
def update_figure_template(theme):
    return px.bar(
        df, x="Fruit", y="Amount", color="City", barmode="group",
        template=template_from_url(theme)
    )


if __name__ == "__main__":
    app.run(debug=True)
