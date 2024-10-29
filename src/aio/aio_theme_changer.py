from dash import html, dcc, Input, Output, State, callback, clientside_callback, MATCH, ClientsideFunction, get_app
from typing import Dict, List

from dash_bootstrap_templates import load_figure_template
import dash_bootstrap_components as dbc
import uuid

dbc_themes_url = {
    item: getattr(dbc.themes, item)
    for item in dir(dbc.themes)
    if not item.startswith(("_", "GRID"))
}
url_dbc_themes = dict(map(reversed, dbc_themes_url.items()))
dbc_themes_lowercase = [t.lower() for t in dbc_themes_url.keys()]
dbc_dark_themes = ["CYBORG", "DARKLY", "SLATE", "SOLAR", "SUPERHERO", "VAPOR"]


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
        store = lambda aio_id: {
            "component": "ThemeChangerAIO",
            "subcomponent": "store",
            "aio_id": aio_id,
        }
        assetsPath = lambda aio_id: {
            "component": "ThemeSwitchAIO",
            "subcomponent": "assetsPath",
            "aio_id": aio_id,
        }

    ids = ids

    def __init__(
            self,
            aio_id: str = str(uuid.uuid4()),
            custom_themes: Dict[str, str] = None,
            custom_dark_themes: List[str] = None,
            radio_props: Dict[str, any] = None,
            button_props: Dict[str, any] = None,
            offcanvas_props: Dict[str, any] = None,
    ):

        """ThemeChangerAIO is an All-in-One component  composed  of a parent `html.Div` with
        the following components as children:

        - `dbc.Button` ("`switch`") Opens the Offcanvas component for user to select a theme.
        - `dbc.Offcanvas` ("`offcanvas`")
        - `dbc.RadioItems` ("`radio`").  The themes are displayed as RadioItems inside the `dbc.Offcanvas` component.
          The `value` is a url for the theme
        - Two `dcc.Store` used as `Input` of the clientside callbacks to provide the theme list and the assets path.

        The ThemeChangerAIO component updates the stylesheet  when the `value` of radio changes. (ie the user selects a new theme)

        - param: `radio_props` A dictionary of properties passed into the dbc.RadioItems component. The default `value` is `dbc.themes.BOOTSTRAP`
        - param: `button_props`  A dictionary of properties passed into the dbc.Button component.
        - param: `offcanvas_props`. A dictionary of properties passed into the dbc.Offcanvas component
        - param: `aio_id` The All-in-One component ID used to generate components' dictionary IDs.
        - param: `custom_themes` A dictionary of local .css files or external url
            with the keys being the theme name and the value being the theme path (file name in assets folder or url).
        - param: `custom_dark_themes` List of custom dark theme name, so that they appear with a black background in the offcanvas list.

        The All-in-One component dictionary IDs are available as:

        - ThemeChangerAIO.ids.radio(aio_id)
        - ThemeChangerAIO.ids.offcanvas(aio_id)
        - ThemeChangerAIO.ids.button(aio_id)
        """
        # make all dash_bootstrap_templates templates available to plotly figures
        load_figure_template("all")

        # concat custom themes and bootstrap themes
        themes_url = {**custom_themes, **dbc_themes_url} if custom_themes else dbc_themes_url
        # concat custom dark themes and bootstrap dark themes
        dark_themes = (dbc_dark_themes + custom_dark_themes) if custom_dark_themes else dbc_dark_themes
        dark_themes_url = [url for theme, url in themes_url.items() if theme in dark_themes]

        # init button_props
        if button_props is None:
            button_props = {}
        # set default params if they don't exist
        button_props.setdefault("children", "Change Theme")
        button_props.setdefault("color", "secondary")
        button_props.setdefault("outline", True)
        button_props.setdefault("size", "sm")

        # init radio_props
        if radio_props is None:
            radio_props = {}
        # set default params if they don't exist
        radio_props.setdefault("options", [{'label': k, 'value': v} for k, v in themes_url.items()])
        radio_props.setdefault("value", dbc.themes.BOOTSTRAP)
        # add label styling to make the difference between light/dark themes
        for option in radio_props['options']:
            option.setdefault(
                "label_id", "theme-switch-label-dark" if option["value"] in dark_themes_url else "theme-switch-label"
            )
        # init offcanvas_props
        if offcanvas_props is None:
            offcanvas_props = {}
        # set default params if they don't exist
        offcanvas_props.setdefault("title", "Select a Theme")
        offcanvas_props.setdefault("is_open", False)
        offcanvas_props.setdefault("style", {
            "width": 'unset',  # so that it can grow if there is a long theme label
            "min-width": 230,
        })
        offcanvas_props.setdefault("children", [
            dbc.RadioItems(id=self.ids.radio(aio_id), **radio_props),
        ])

        super().__init__([
            dbc.Button(id=self.ids.button(aio_id), **button_props),
            dbc.Offcanvas(id=self.ids.offcanvas(aio_id), **offcanvas_props),
            dcc.Store(id=self.ids.store(aio_id), data=themes_url),
            dcc.Store(id=self.ids.assetsPath(aio_id), data=get_app().config.assets_url_path)
        ])

    @callback(
        Output(ids.offcanvas(MATCH), "is_open"),
        Input(ids.button(MATCH), "n_clicks"),
        State(ids.offcanvas(MATCH), "is_open"),
    )
    def toggle_theme_offcanvas(n1, is_open):
        return not is_open if n1 else is_open

    clientside_callback(
        """
        function (selected_theme, themes, assetsUrlPath) {

            // function to test if the theme is an external or a local theme
            const isValidHttpUrl = (theme) => {
                try {
                    new URL(theme);
                    return true;
                } catch (error) {
                    return false;
                }
            }
        
            // Find the existing theme stylesheets
            let stylesheets = []
            Object.values(themes).forEach(

                url => stylesheets.push(...document.querySelectorAll(`link[rel='stylesheet'][href*='${url}']`))
            );

            // Create a new stylesheet link element
            let newStylesheet = document.createElement("link");
            newStylesheet.rel = "stylesheet";
            newStylesheet.href = isValidHttpUrl(selected_theme)
                ? selected_theme
                : `/${assetsUrlPath}/${selected_theme.split('/').at(-1)}`;


            // When the new stylesheet is loaded, remove the old ones
            newStylesheet.onload = function () {

                stylesheets.forEach(s => s.remove());
            }

            // Append the new stylesheet to the document head
            document.head.appendChild(newStylesheet);

            return window.dash_clientside.no_update;
        }
        """,
        Output(ids.store(MATCH), "id"),
        Input(ids.radio(MATCH), "value"),
        Input(ids.store(MATCH), "data"),
        State(ids.assetsPath(MATCH), "data")
    )

    # This callback is used to bundle custom CSS with the AIO component. This only runs once when the app starts.
    # The clientside function adds the css to a <style> element and appends it to the <head>.
    # Dash requires callbacks to have an Output even if there is nothing to update.
    clientside_callback(
        """
        function(id) {
            let style = document.createElement('style')
            style.innerText = `
                #theme-switch-label-dark {
                    background-color: black;
                    color: white;
                    width: 100px
                }                
                #theme-switch-label {
                    background-color: white;
                    color: black;
                    width: 100px
                }
            `
            document.head.appendChild(style)
        }
        """,
        Output(ids.offcanvas(MATCH), "id"),
        Input(ids.offcanvas(MATCH), "id"),
    )
