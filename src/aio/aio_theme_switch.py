from dash import html, dcc, Input, Output, State, callback, clientside_callback, MATCH
import dash_bootstrap_components as dbc
import uuid

dbc_themes_url = {
    item: getattr(dbc.themes, item)
    for item in dir(dbc.themes)
    if not item.startswith(("_", "GRID"))
}
url_dbc_themes = dict(map(reversed, dbc_themes_url.items()))
dbc_themes_lowercase = [t.lower() for t in dbc_themes_url.keys()]


class ThemeSwitchAIO(html.Div):
    class ids:
        switch = lambda aio_id: {
            "component": "ThemeSwitchAIO",
            "subcomponent": "switch",
            "aio_id": aio_id,
        }
        store = lambda aio_id: {
            "component": "ThemeSwitchAIO",
            "subcomponent": "store",
            "aio_id": aio_id,
        }
        dummy_div = lambda aio_id: {
            "component": "ThemeSwitchAIO",
            "subcomponent": "dummy_div",
            "aio_id": aio_id,
        }

    ids = ids

    def __init__(
        self,
        themes=None,
        icons=None,
        switch_props={},
        aio_id=None,
    ):
        """ThemeSwitchAIO is an All-in-One component  composed  of a parent `html.Div` with
        the following components as children:

        - `dbc.Switch` ("`switch`") with icons to the left and right of the switch.
        - `dcc.Store` ("`store`") The `themes` are stored in the `data` prop.
        - `html.Div` is used as the `Output` of the clientside callbacks.

        The ThemeSwitchAIO component updates the stylesheet when triggered by changes to the `value` of `switch` or when
        the themes are updated in the "`store`" component.  The themes in the switch may be updated in a callback
        by changing the theme urls in the "`store`" component.

        - param: `themes` A list of two urls for the external stylesheets. The default is `[dbc.themes.CYBORG, dbc.themes.BOOTSTRAP]`.
        - param: `icons`  A dict of the icons to the left and right of the switch. The default is
          `{"left" :"fa fa-moon", "right" :"fa fa-sun"}`.
        - param: `aio_id` The All-in-One component ID used to generate components' dictionary IDs.

        The All-in-One component dictionary IDs are available as

        - ThemeSwitchAIO.ids.switch(aio_id)
        - ThemeSwitchAIO.ids.store(aio_id)
        """
        from dash_bootstrap_templates import load_figure_template

        load_figure_template(dbc_themes_lowercase)

        if aio_id is None:
            aio_id = str(uuid.uuid4())

        if themes is None:
            themes = [dbc.themes.CYBORG, dbc.themes.BOOTSTRAP]
        if icons is None:
            icons = {"left": "fa fa-moon", "right": "fa fa-sun"}

        switch_props = switch_props.copy()
        if "value" not in switch_props:
            switch_props["value"] = True
        if "className" not in switch_props:
            switch_props["className"] = "d-inline-block ms-1"

        super().__init__(
            [
                html.Span(
                    [
                        dbc.Label(className=icons["left"]),
                        dbc.Switch(id=self.ids.switch(aio_id), **switch_props),
                        dbc.Label(className=icons["right"]),
                    ],
                ),
                dcc.Store(id=self.ids.store(aio_id), data=themes),
                html.Div(id=self.ids.dummy_div(aio_id)),
            ]
        )

    clientside_callback(
        """
        function toggle(theme_switch, url) {
          var themeLink = theme_switch ? url[0] : url[1];
          var stylesheets = document.querySelectorAll(
            `link[rel=stylesheet][href^="https://cdn.jsdelivr.net/npm/bootswatch@5"],
            link[rel=stylesheet][href^="https://cdn.jsdelivr.net/npm/bootstrap@5"]`
          );
          // The delay in updating the stylesheet reduces the flash when changing themes
          stylesheets[stylesheets.length - 1].href = themeLink          
          setTimeout(function() {
            for (let i = 0; i < stylesheets.length -1; i++) {
              stylesheets[i].href = themeLink;
            }
          }, 500);   
        }
        """,
        Output(ids.dummy_div(MATCH), "children"),
        Input(ids.switch(MATCH), "value"),
        Input(ids.store(MATCH), "data"),
    )

    # This callback is used to do the initial load of the
    # stylesheet and the default icons for the toggle switch.
    # This callback just needs to run once
    # when the app starts.  Dash requires callbacks to have an Output
    # even if there is nothing to update.
    #
    clientside_callback(
        """
        function(theme_switch, theme_urls) {            
            var themeLink = theme_switch ? theme_urls[0] : theme_urls[1];
            let urls = [
                "https://use.fontawesome.com/releases/v5.15.4/css/all.css",
                themeLink
            ];
            for (const url of urls) {
                var link = document.createElement("link");

                link.type = "text/css";
                link.rel = "stylesheet";
                link.href = url;

                document.head.appendChild(link);
            }
        }
        """,
        Output(ids.dummy_div(MATCH), "role"),
        Input(ids.switch(MATCH), "value"),
        Input(ids.store(MATCH), "data"),
    )
