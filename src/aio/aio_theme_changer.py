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
dbc_dark_themes = ["cyborg", "darkly", "slate", "solar", "superhero", "vapor"]


def template_from_url(url):
    """ returns the name of the plotly template for the Bootstrap stylesheet url"""
    return url_dbc_themes.get(url, "bootstrap").lower()


class ThemeChangerAIO(html.Div):
    class ids:
        button = lambda aio_id: {
            "component": "ThemeChangerAIO",
            "subcomponent": "button",
            "aio_id": aio_id,
        }
        offcanvas = lambda aio_id: {
            "component": "ThemeChangerAIO",
            "subcomponent": "offcanvas",
            "aio_id": aio_id,
        }
        radio = lambda aio_id: {
            "component": "ThemeChangerAIO",
            "subcomponent": "radio",
            "aio_id": aio_id,
        }
        dummy_div = lambda aio_id: {
            "component": "ThemeChangerAIO",
            "subcomponent": "dummy_div",
            "aio_id": aio_id,
        }

    ids = ids

    def __init__(
        self, radio_props={}, button_props={}, offcanvas_props={}, aio_id=None,
    ):

        """ThemeChangerAIO is an All-in-One component  composed  of a parent `html.Div` with
        the following components as children:

        - `dbc.Button` ("`switch`") Opens the Offcanvas component for user to select a theme.
        - `dbc.Offcanvas` ("`offcanvas`")
        - `dbc.RadioItems` ("`radio`").  The themes are displayed as RadioItems inside the `dbc.Offcanvas` component.
          The `value` is a url for the theme
        - `html.Div` is used as the `Output` of the clientside callbacks.

        The ThemeChangerAIO component updates the stylesheet  when the `value` of radio changes. (ie the user selects a new theme)

        - param: `radio_props` A dictionary of properties passed into the dbc.RadioItems component. The default `value` is `dbc.themes.BOOTSTRAP`
        - param: `button_props`  A dictionary of properties passed into the dbc.Button component.
        - param: `offcanvas_props`. A dictionary of properties passed into the dbc.Offcanvas component
        - param: `aio_id` The All-in-One component ID used to generate components' dictionary IDs.

        The All-in-One component dictionary IDs are available as:

        - ThemeChangerAIO.ids.radio(aio_id)
        - ThemeChangerAIO.ids.offcanvas(aio_id)
        - ThemeChangerAIO.ids.button(aio_id)
        """
        from dash_bootstrap_templates import load_figure_template

        load_figure_template("all")

        if aio_id is None:
            aio_id = str(uuid.uuid4())

        radio_props = radio_props.copy()
        if "value" not in radio_props:
            radio_props["value"] = dbc_themes_url["BOOTSTRAP"]
        if "options" not in radio_props:
            radio_props["options"] = [
                {
                    "label": str(i),
                    "label_id": "theme-switch-label",
                    "value": dbc_themes_url[i],
                }
                for i in dbc_themes_url
            ]
            # assign id to dark themes in order to apply css
            for option in radio_props["options"]:
                if option["label"].lower() in dbc_dark_themes:
                    option["label_id"] = "theme-switch-label-dark"

        button_props = button_props.copy()
        if "children" not in button_props:
            button_props["children"] = "Change Theme"
        if "color" not in button_props:
            button_props["color"] = "secondary"
        if "outline" not in button_props:
            button_props["outline"] = True
        if "size" not in button_props:
            button_props["size"] = "sm"

        offcanvas_props = offcanvas_props.copy()
        if "children" not in offcanvas_props:
            offcanvas_props["children"] = [
                dbc.RadioItems(id=self.ids.radio(aio_id), **radio_props),
            ]
        if "title" not in offcanvas_props:
            offcanvas_props["title"] = "Select a Theme"
        if "is_open" not in offcanvas_props:
            offcanvas_props["is_open"] = False
        if "style" not in offcanvas_props:
            offcanvas_props["style"] = {"width": 235}

        super().__init__(
            [
                dbc.Button(id=self.ids.button(aio_id), **button_props),
                dbc.Offcanvas(id=self.ids.offcanvas(aio_id), **offcanvas_props),
                html.Div(
                    id=self.ids.dummy_div(aio_id),
                    children=radio_props["value"],
                    hidden=True,
                ),
            ]
        )

    @callback(
        Output(ids.offcanvas(MATCH), "is_open"),
        Input(ids.button(MATCH), "n_clicks"),
        [State(ids.offcanvas(MATCH), "is_open")],
    )
    def toggle_theme_offcanvas(n1, is_open):
        if n1:
            return not is_open
        return is_open

    clientside_callback(
        """
        function switcher(url) {
          var stylesheets = document.querySelectorAll(
            `link[rel=stylesheet][href^="https://cdn.jsdelivr.net/npm/bootswatch@5"],
            link[rel=stylesheet][href^="https://cdn.jsdelivr.net/npm/bootstrap@5"]`
          );
          // The delay in updating the stylesheet reduces the flash when changing themes
          stylesheets[stylesheets.length - 1].href = url          
          setTimeout(function() {
            for (let i = 0; i < stylesheets.length -1; i++) {
              stylesheets[i].href = url;
            }
          }, 500);            
        }
        """,
        Output(ids.dummy_div(MATCH), "key"),
        Input(ids.radio(MATCH), "value"),
    )

    # This callback is used to bundle custom CSS with the AIO component
    # and to add a stylesheet so that the theme switcher will work even if there is a
    # Bootstrap stylesheet in the assets folder.
    # This only runs once when the app starts. The clientside function adds the css to a <style>
    # element and appends it to the <head>.  Dash requires callbacks to have an Output
    # even if there is nothing to update.
    #
    clientside_callback(
        """
        function(url) {
            var style = document.createElement('style')
            const aio_css = `
              #theme-switch-label-dark {
              background-color: black;
              color: white;
              width: 100px
            }            
            #theme-switch-label {
              background-color: white;
              color: black;
              width: 100px            
            `            
            style.innerText = aio_css            
            document.head.appendChild(style)
            
            // initialize theme
            var link = document.createElement("link");            
            link.type = "text/css";
            link.rel = "stylesheet";
            link.href = url;
            document.head.appendChild(link);
        }
        """,
        Output(ids.dummy_div(MATCH), "role"),
        Input(ids.dummy_div(MATCH), "children"),
    )
