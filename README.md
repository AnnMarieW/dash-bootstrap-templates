# Dash Bootstrap Templates


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

```python

from dash import Dash, dcc, html
import plotly.express as px
import dash_bootstrap_components as dbc

from dash_bootstrap_templates import load_figure_template

app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
load_figure_template("bootstrap")


df = px.data.gapminder().query("continent != 'Asia'")  # remove Asia for visibility
fig = px.line(df, x="year", y="lifeExp", color="continent", line_group="country")


app.layout = dbc.Container(
    [
        html.H1("Dash Bootstrap Template Demo", className="bg-primary text-white p-2"),
        dbc.Row(dbc.Col(dcc.Graph(figure=fig))),
    ],
    fluid=True,
)


if __name__ == "__main__":
    app.run_server(debug=True)

```
![image](https://user-images.githubusercontent.com/72614349/115889093-7c7a1000-a408-11eb-8bff-7773327016e8.png)



## Demo App 2 - 4 Graphs Updated

This demo [(code here)](https://github.com/AnnMarieW/dash-bootstrap-templates/blob/main/examples/demo_4_graphs.py),
shows how the theme is applied to all 4 graphs.

![figure_template2](https://user-images.githubusercontent.com/72614349/129459807-30c22ffe-7a8c-44b9-9555-6cfd50ec355b.png)

## Theme Switcher Components

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

app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])


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
    className="m-4",
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