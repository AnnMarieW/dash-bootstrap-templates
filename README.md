# Dash Bootstrap Templates

Dash Bootstrap Templates is a collection of Plotly figure templates that
are customized for Bootstrap themes.

There are templates for each of the 22 themes available in the [Dash Bootstrap
Components Library](https://dash-bootstrap-components.opensource.faculty.ai/)


## Background

One of the nice features in [Dash Labs]() is how it creates the Bootstrap figure templates. 
In the demo apps below, the figure on the left is using these templates.  As you can see, it 
creates graphs with colorways and fonts that are consistent with your selected Bootstrap theme.
In Dash Labs, these templates are created on-the-fly by setting figure_template=True, 
in certain layout templates.   

This library makes these figure templates available for use
in a Dash app the same way as any other build-in Plotly figure templated.   It does this by
using the Dash Labs algorithms to generate the 22 most common Bootstrap figure
templates and saves them in a json format.   The load_figure_template() function reads the json
file, adds it to plotly.io and sets it as the default template for an app.

Here are the advantages of this method rather than creating the templates on-the-fly:

- It makes these templates available for use in any app using Dash or any of the Dash Labs layout
  templates. Currently, these are available only in a few of the Dash Labs layout templates.
-  Since the templates are not create on-the-fly, it increases app performance and 
   eliminates the risk that the template fail to build.
-  It eliminates runtime dependency of tinycss2 and spectra. (Those are only used to create the templates 
   that are included in this library)


## Demo Apps
### Dash Bootstrap Figure Template VS The Plotly default

#### demo_minty.py  [See the code](https://github.com/AnnMarieW/dash-bootstrap-templates/blob/main/demo_minty.py)
![image](https://user-images.githubusercontent.com/72614349/115800602-d4286500-a38f-11eb-90d3-b6c96f5367ae.png)

---
---
#### demo_superhero.py  [See the code](https://github.com/AnnMarieW/dash-bootstrap-templates/blob/main/demo_superhero.py)
![image](https://user-images.githubusercontent.com/72614349/115800753-1a7dc400-a390-11eb-941d-3fe1de842ce6.png)
---
---

#### demo_sketchy.py [See the code](https://github.com/AnnMarieW/dash-bootstrap-templates/blob/main/demo_sketchy.py)
![image](https://user-images.githubusercontent.com/72614349/115800865-45681800-a390-11eb-9e69-2b6ea0c7538c.png)




## Available Themes

This library has figure templates for the following Bootstrap/Bootswatch themes:

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
]
