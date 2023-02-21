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

        - param: `switch_props` A dictionary of properties passed into the dbc.Switch component.
        - param: `themes` A list of two urls for the external stylesheets or pathnames to files.
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
            themes = [dbc.themes.BOOTSTRAP, dbc.themes.CYBORG]
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
          // save variables and variable paths of target and old stylesheets
          var themeLink = theme_switch ? url[0] : url[1];
          var oldThemeLink = theme_switch ? url[1]: url[0];
          var testString = "link[rel='stylesheet'][href*='" + oldThemeLink + "'],"
            testString += "link[rel='stylesheet'][href*='" + themeLink + "'],"
            testString += "link[rel='stylesheet'][data-href*='" + oldThemeLink + "'],"
            testString += "link[rel='stylesheet'][data-href*='" + themeLink + "']"
            
          // Find style sheets matching the targets listed above
          var stylesheets = document.querySelectorAll(testString);
               
          setTimeout(function() {
            // If stylesheets are found, then loop through and update old to data-href and new to href from data-href
            // data-href  is a temporary holding spot to save the old theme link.
            // This prevents the screen from flashing when the theme changes.
            if (stylesheets) {
                for (let i = 0; i < stylesheets.length; i++) {
                    if (!stylesheets[i].getAttribute('data-href')) {
                        stylesheets[i].setAttribute('data-href', '')
                    }
                    if (stylesheets[i].href.includes(themeLink) || stylesheets[i].getAttribute('data-href').includes(themeLink)) {
                        if (stylesheets[i]['data-href']) {
                            stylesheets[i].href = stylesheets[i]['data-href'];
                        } else {
                            stylesheets[i].href = themeLink;
                        }
                        stylesheets[i].setAttribute('data-href', '')
                    }
                    else if (stylesheets[i].href.includes(oldThemeLink) || stylesheets[i].getAttribute('data-href').includes(oldThemeLink)) {
                        setTimeout(function () {
                        if (stylesheets[i]['href']) {
                            stylesheets[i].setAttribute('data-href', stylesheets[i]['href']);
                        } else {
                            stylesheets[i].setAttribute('data-href', oldThemeLink)
                        }
                        stylesheets[i]['href'] = ''
                        }, 100)
                    }
                };
            }
            // Test if theme was applied, if not add stylesheet
            var stylesheet = document.querySelectorAll('link[rel="stylesheet"][href*="'+ themeLink + '"]')
            if (stylesheet.length == 0) {
                var newLink = document.createElement('link');
                newLink.rel = 'stylesheet';
                newLink.href = themeLink;
                newLink.setAttribute('data-href', '');
                document.head.appendChild(newLink);
            }
          }, 100);   
        }
        """,
        Output(ids.dummy_div(MATCH), "children"),
        Input(ids.switch(MATCH), "value"),
        Input(ids.store(MATCH), "data"),
    )

    # This callback is used to do the initial load of the
    # default icons for the toggle switch.
    # This callback just needs to run once
    # when the app starts.  Dash requires callbacks to have an Output
    # even if there is nothing to update.
    #
    clientside_callback(
        """
        // apply font awesome defaults
        function(id) {            
            let url = "https://use.fontawesome.com/releases/v5.15.4/css/all.css";
            var link = document.createElement("link");

            link.type = "text/css";
            link.rel = "stylesheet";
            link.href = url;

            document.head.appendChild(link);
        }
        """,
        Output(ids.dummy_div(MATCH), "role"),
        Input(ids.dummy_div(MATCH), "role"),
    )
