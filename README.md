# Dash Bootstrap Templates

#### See these features live at : https://hellodash.pythonanywhere.com/theme_explorer


`dash-bootstrap-templates` library provides: 

- **Bootstrap themed Plotly figure templates**. You will find a Plotly template for each of the 26 Bootstrap/Bootswatch themes available in the
[Dash Bootstrap Components Library](https://dash-bootstrap-components.opensource.faculty.ai/). These templates will automatically style your figures with Bootstrap theme colors and fonts.

- **Two  [All-in-One](https://dash.plotly.com/all-in-one-components) components** to change themes in a Dash app.
  - `ThemeSwitchAIO` toggles between two themes. 
  - `ThemeChangerAIO` select from multiple themes.

- **The dbc.css stylesheet** which styles Dash Core Components and the Dash DataTable with a Bootstrap theme.

> Note:  The `ThemeSwitchAIO` and `ThemeChangerAIO` components  and the `dbc.css` stylesheet requires  Dash Bootstrap Components>=V1.0.0.  It will only
> work with the themes included in Dash Bootstrap Components>=V1.0.0.


## Figure Template Quickstart
```python"
pip install dash-bootstrap-templates
```
> Learn more about Plotly figure templates and themes at: https://plotly.com/python/templates/
```python
"""
A sample of 8 of the 26 Bootstrap themed Plotly figure templates available
in the dash-bootstrap-template library

"""
from dash import Dash, html, dcc
import dash_bootstrap_components as dbc
from dash_bootstrap_templates import load_figure_template
import plotly.express as px

df = px.data.gapminder()

templates = [
    "bootstrap",
    "minty",
    "pulse",
    "flatly",
    "quartz",
    "cyborg",
    "darkly",
    "vapor",
]

load_figure_template(templates)

figures = [
    px.scatter(
        df.query("year==2007"),
        x="gdpPercap",
        y="lifeExp",
        size="pop",
        color="continent",
        log_x=True,
        size_max=60,
        template=template,
        title="Gapminder 2007: '%s' theme" % template,
    )
    for template in templates
]

app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = dbc.Container([dcc.Graph(figure=fig, className="m-4") for fig in figures])

if __name__ == "__main__":
    app.run_server(debug=True)
```

![image](https://user-images.githubusercontent.com/72614349/143956424-9e172c03-139e-4126-bed5-b1800ad7e17a.png)
![image](https://user-images.githubusercontent.com/72614349/143956545-769a00f8-92a3-44aa-8718-bdbb32b2464e.png)
![image](https://user-images.githubusercontent.com/72614349/143956649-32b620c7-231a-4de6-ad3a-8fb0863da2a4.png)
![image](https://user-images.githubusercontent.com/72614349/143956713-7fdbed38-6799-472b-87ba-d863481c6525.png)



![figure_template2](https://user-images.githubusercontent.com/72614349/129459807-30c22ffe-7a8c-44b9-9555-6cfd50ec355b.png)

## dbc.css  stylesheet

The `dash-core-components`, the Dash `DataTable` and Plotly figures are not automatically styled with a Bootstrap theme.
An easy way to make your Dash components look better with a Bootstrap theme is to use the stylesheet from
 the [dash-bootstrap-templates](https://github.com/AnnMarieW/dash-bootstrap-templates) library. This stylesheet defines the "dbc" class.

Adding `className="dbc"` minimally styles Dash components with your selected Bootstrap theme:
- Makes the text readable in both light and dark themes.
- Uses theme's font-family.
- Changes the accent color to the theme's primary color


You can add the dbc class as an external stylesheet like this:
```
dbc_css = ("https://cdn.jsdelivr.net/gh/AnnMarieW/dash-bootstrap-templates@V1.0.2/dbc.min.css")
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP, dbc_css])

```


Add  `className="dbc"` to the outer container of the app or a component like this:
```
app.layout = dbc.Container(
    [
        ...
    ],
    fluid=True,
    className="dbc"
)
```

**That's it!** Simply adding `className="dbc"` will make Dash Core Components and the DataTable look better with **ALL** themes included in the `dash-bootstrap-components` library.
> See a live demo at: https://hellodash.pythonanywhere.com/about_dbc_css

If you have suggestion for improvements or if you find a bug, please let us know on the [issue tracker](https://github.com/AnnMarieW/dash-bootstrap-templates/issues)

**Requires `dash-bootstrap-components>=V1.0.0`**


## Theme Switcher Components

> See a live demo at https://hellodash.pythonanywhere.com/theme_change_components

`dash-bootstrap-templates` has two [All-in-One](https://dash.plotly.com/all-in-one-components) components to change themes. 
The `ThemeSwitchAIO` is a switch with icons on the left and right, which is ideal for toggling between a light and a dark theme. 
The `ThemeChangerAIO` has a button that opens an `dbc.Offcanvas` component which by default shows all the available themes.

Note the All-in-One component switches the Bootstrap stylesheet for the app and sets the default Plotly figure template
for the theme, however, figures must be updated in a callback in order to render the figure with the new template.
See the callback below for an example.  The `template_from_url` is a helper function that returns the template name
based on the theme url.  For example `template_from_ur(dbc.themes.SLATE)` returns `"slate"`



## ThemeChangerAIO Quickstart
```python

from dash import Dash, dcc, html, Input, Output
import pandas as pd
import plotly.express as px
import dash_bootstrap_components as dbc
from dash_bootstrap_templates import ThemeChangerAIO, template_from_url


dbc_css = (
    "https://cdn.jsdelivr.net/gh/AnnMarieW/dash-bootstrap-templates@V1.0.1/dbc.min.css"
)
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP, dbc_css])


df = pd.DataFrame(
    {
        "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
        "Amount": [4, 1, 2, 2, 4, 5],
        "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"],
    }
)
header = html.H4(
    "ThemeChangerAIO Demo", className="bg-primary text-white p-4 mb-2 text-center"
)
buttons = html.Div(
    [
        dbc.Button("Primary", color="primary"),
        dbc.Button("Secondary", color="secondary"),
        dbc.Button("Success", color="success"),
        dbc.Button("Warning", color="warning"),
        dbc.Button("Danger", color="danger"),
        dbc.Button("Info", color="info"),
        dbc.Button("Light", color="light"),
        dbc.Button("Dark", color="dark"),
        dbc.Button("Link", color="link"),
    ],
    className="m-4",
)
graph = html.Div(dcc.Graph(id="graph"), className="m-4")

app.layout = dbc.Container(
    [
        header,
        dbc.Row(
            [
                dbc.Col(ThemeChangerAIO(aio_id="theme", radio_props={"value":dbc.themes.FLATLY}), width=2,),
                dbc.Col([buttons, graph],width=10),
            ]
        ),
    ],
    className="m-4 dbc",
    fluid=True,
)


@app.callback(
    Output("graph", "figure"), Input(ThemeChangerAIO.ids.radio("theme"), "value"),
)
def update_graph_theme(theme):
    return px.bar(
        df, x="Fruit", y="Amount", color="City", barmode="group", template=template_from_url(theme)
    )


if __name__ == "__main__":
    app.run_server(debug=True)

```

![theme_changer](https://user-images.githubusercontent.com/72614349/141466834-6b02f478-cae8-4927-b05e-be0e98cb61df.gif)

---------
```python

```
Here is the same app, but using a the `ThemeSwitchAIO` component to toggle between two themes.
See the  [(code here)](https://github.com/AnnMarieW/dash-bootstrap-templates/blob/main/examples/demo_toggle.py).

It's also possible to change the icons.  See an example of using Bootstrap icons instead of the default FontAwesome
icons [here](https://github.com/AnnMarieW/dash-bootstrap-templates/blob/main/examples/demo_toggle_icons.py).

![theme_toggle](https://user-images.githubusercontent.com/72614349/141466191-13709102-a2fb-45b5-a984-383d3e6ab373.gif)




## Background

[Dash Labs](https://community.plotly.com/t/introducing-dash-labs/52087) is Plotly library that explores new features for future releases of Dash. 
In Dash Labs V0.4.0, there was a cool feature where Bootstrap themed figure templates were created "on the fly". This was a
part of the layout templates project that is no longer being developed.    

Even though these Bootstrap themed figure templates will not be included in Dash, the `dash-bootstrap-templates` makes
them available to you. The figure templates are created using the Dash Labs' algorithms and saved in json format.  When 
you use `load_figure_template()` in your app, it loads the json file, adds it to `plotly.io` and sets it as the default figure template for an app.  See more 
information about  Plotly figure templates [here](https://plotly.com/python/templates/).


## Available Themes

This library provides a figure template for the following Bootstrap/Bootswatch themes:

valid_themes = [
    "bootstrap",
    "cerulean",
    "cosmo",
    "flatly",
    "journal",
    "litera",
    "lumen",
    "lux",
    "materia",
    "minty",
    "pulse",
    "sandstone",
    "simplex",
    "sketchy",
    "spacelab",
    "united",
    "yeti",
    "cyborg",
    "darkly",
    "slate",
    "solar",
    "superhero",
    "morph",
    "quartz",
    "vapor"
    "zephyr"
]


## ThemeChangerAIO Reference
**ThemeChangerAIO** is an All-in-One component  composed  of a parent `html.Div` with
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
    

## ThemeSwitchAIO Reference

**ThemeSwitchAIO** is an All-in-One component  composed  of a parent `html.Div` with the following components as children:

- `dbc.Switch` ("`switch`") with icons to the left and right of the switch.
- `dcc.Store` ("`store`") The `themes` are stored in the `data` prop.
- `html.Div` is used as the `Output` of the clientside callbacks.

The ThemeSwitchAIO component updates the stylesheet when triggered by changes to the `value` of `switch` or when
the themes are updated in the "`store`" component.  The themes in the switch may be updated in a callback
by changing the theme urls in the "`store`" component.

- param: `themes` A list of two urls for the external stylesheets. The default is `[dbc.themes.CYBORG, dbc.themes.BOOTSTRAP]`.
- param: `icons`  A dict of the icons to the left and right of the switch. The default is  
  `{"left" :"fa fa-moon", "right" :"fa fa-sun"}`.
- param: `aio_id` The All-in-One component ID used to generate component's dictionary IDs.

The All-in-One component dictionary IDs are available as
- ThemeSwitchAIO.ids.switch(aio_id)
- ThemeSwitchAIO.ids.store(aio_id)

---

### Contributors
Special thanks to @tcbegley and @emilhe for their help with this project.