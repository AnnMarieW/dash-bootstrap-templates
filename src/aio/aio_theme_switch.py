from dash import html, dcc, Input, Output, clientside_callback, MATCH, ClientsideFunction, get_app
import dash_bootstrap_components as dbc
import uuid
from dash_bootstrap_templates import load_figure_template


class ThemeSwitchAIO(html.Div):
    class ids:
        switch = lambda aio_id: {
            "component": "ThemeSwitchAIO",
            "subcomponent": "switch",
            "aio_id": aio_id,
        }
        leftIcon = lambda aio_id: {
            "component": "ThemeSwitchAIO",
            "subcomponent": "leftIcon",
            "aio_id": aio_id,
        }
        rightIcon = lambda aio_id: {
            "component": "ThemeSwitchAIO",
            "subcomponent": "rightIcon",
            "aio_id": aio_id,
        }
        store = lambda aio_id: {
            "component": "ThemeSwitchAIO",
            "subcomponent": "store",
            "aio_id": aio_id,
        }

    ids = ids

    def __init__(
            self,
            aio_id: str = str(uuid.uuid4()),
            themes: tuple[str, str] | str = (dbc.themes.CYBORG, dbc.themes.BOOTSTRAP),
            icons=None,
            switch_props: dict[str, any] = None,
    ):
        """ThemeSwitchAIO is an All-in-One component  composed  of a parent `html.Div` with
        the following components as children:

        - `dbc.Switch` ("`switch`") with icons to the left and right of the switch.
        - `dcc.Store` ("`store`") The `themes` are stored in the `data` prop.
        - `html.Div` is used as the `Output` of the clientside callbacks.

        The ThemeSwitchAIO component updates the stylesheet when triggered by changes to the `value` of `switch` or when
        the themes are updated in the "`store`" component.  The themes in the switch may be updated in a callback
        by changing the theme urls in the "`store`" component.

        - param: `switch_props` A dictionary of properties passed into the dbc.Switch component.
        - param: `themes` A list of two urls for the external stylesheets or pathnames to files.
        - param: `icons`  A dict of the icons to the left and right of the switch. The default is
          `{"left" :"fa fa-moon", "right" :"fa fa-sun"}`.
        - param: `aio_id` The All-in-One component ID used to generate components' dictionary IDs.

        The All-in-One component dictionary IDs are available as

        - ThemeSwitchAIO.ids.switch(aio_id)
        - ThemeSwitchAIO.ids.store(aio_id)
        """

        # init icons and switch_props
        if icons is None:
            icons = {"left": "fa fa-moon", "right": "fa fa-sun"}
        if switch_props is None:
            switch_props = {}
        # set "value" and "className" if they don't exist
        switch_props.setdefault("value", True)
        switch_props.setdefault("className", "d-inline-block ms-1")

        # add fontawesome resource for the icons and dbc.css to apply Bootstrap theme to dcc, DataTable and Dash AG Grid
        app = get_app()
        app.config.external_stylesheets += [
            "https://use.fontawesome.com/releases/v5.15.4/css/all.css",
            # "https://cdn.jsdelivr.net/gh/AnnMarieW/dash-bootstrap-templates/dbc.min.css"
        ]

        # if using custom themes in /assets, filter them out to not be automatically imported by Dash
        # and let the switch handle them.
        # append "|" if assets_ignore has already regex rules
        if app.config.assets_ignore:
            app.config.assets_ignore += "|"
        # add the themes to ignore in /assets
        if isinstance(themes, str):
            app.config.assets_ignore += f'{themes.replace("/assets/", "")}'
        else:
            app.config.assets_ignore += f'{themes[0].replace("/assets/", "")}|{themes[1].replace("/assets/", "")}'

        # make all dash_bootstrap_templates templates available to plotly figures
        load_figure_template('all')

        super().__init__(
            [
                html.Span(
                    [
                        dbc.Label(id=self.ids.leftIcon(aio_id), className=icons["left"]),
                        dbc.Switch(id=self.ids.switch(aio_id), **switch_props),
                        dbc.Label(id=self.ids.rightIcon(aio_id), className=icons["right"]),
                    ],
                ),
                dcc.Store(id=self.ids.store(aio_id), data=themes)
            ]
        )

    # callback called once, when the switch is created,
    # to apply the 'dbc' class to the outermost dash app container
    clientside_callback(
        ClientsideFunction('themeSwitch', 'applyDbcClass'),
        Output(ids.switch(MATCH), "id"),
        Input(ids.switch(MATCH), "id"),
    )

    clientside_callback(
        ClientsideFunction('themeSwitch', 'toggleTheme'),
        Output(ids.store(MATCH), "id"),
        Input(ids.switch(MATCH), "value"),
        Input(ids.store(MATCH), "data"),
    )
