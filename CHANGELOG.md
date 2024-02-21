
## Feb 21, 2024
Fixed dbc.css
 - use new Bootstrap variables for border width and color  Closes [#6](https://github.com/AnnMarieW/dash-bootstrap-templates/issues/6)
 - matched dcc date picker input fields to match dcc.Dropdown input fields



## Jan 27, 2024
Fixed dbc.css - ag grid toolip background color

## 1.1.2 Jan 14, 2024
Fixed regression where figure background did not match theme's card color.  Closes issue #25


## 1.1.1 Oct 18, 2023

Fixed error in how colorways were created, resulting in a slight changed in the color of the green (Bootstrap Success) color.
Thanks to @oliverb for PR #22


## Oct 2, 2023

Fixed placeholder text color. Closes #20

## 1.1.0 Sept 26, 2023
### New Features

- Added 26 new dark mode figure templates for each of the 26 Bootstrap themed figure templates
-  Added examples of how to use the Bootstrap Color Modes  switch between dark and light modes in a Dash app
- Added support for styling Dash AG Grid with a bootstrap theme in the  `dbc.css` file
-  Added an option to load all figure templates:
```python
from dash_bootstrap_templates import load_figure_template
load_figure_template("all")
```


## Sept 12, 2023

Updated the dbc.css file to add the `dbc-ag-grid` class to apply Bootstrap theme to Dash AG Grid


## 1.0.8 Feb 21, 2023
### Fixed and Added New Features  

- Pull Request  [#14](https://github.com/AnnMarieW/dash-bootstrap-templates/pull/14).  Thanks @BSd3v for the contribution!
- Fixed `ThemeSwitchAIO` so it doesn't load multiple stylesheets when toggling.
- Add support for `ThemeSwitchAIO` to work with stylesheets in the assets folder.
- Removed restriction for `ThemeSwitchAIO` of only working with the themes in the dash-bootstrap-components library.


## 1.0.7  Sept 25, 2022
### Fixed
 - Fixed hover template font  closes [#9](https://github.com/AnnMarieW/dash-bootstrap-templates/issues/9)
 - Fixed margins - made margins the same as the Plotly default templates.


## 1.0.6  Jul 21, 2022
### Fixed
 - Fixed the theme switch component when it starts in dark mode.  closes [#8](https://github.com/AnnMarieW/dash-bootstrap-templates/issues/8)


## 1.0.5 Feb 14, 2022
### Fixed
- relaxed install versions

## 1.0.2

### Changes
 - updated the dbc.css to improve style when switching themes.


## 1.0.0
V1.0.0 is based on `dash` V2.0.0 and `dash-bootstrap-components` V1.0.0 which uses
Boostrap V5 stylesheets.

### Added
 - added "QUARTZ", "MORPH", "VAPOR", "ZEPHYR" themes
 - added 2 All-In-One components to switch themes. 
   - `ThemeSwitchAIO` toggles between two themes
   - `ThemeChangerAIO` opens a Offcanvas component to select any of the 26 themes
   - `template_from_url` helper function to get the figure template name for the selected theme
 - added `dbc.css` which minimally styles `dash-core-components` and the `DataTable` with  the selected Bootstrap theme
 - added examples of the2 AIO components that switch themes.

### Changes
 - updated `_create_templates.py` to generate figure templates based on Boostrap V5 stylesheets


## 0.1.1

This is the initial release of `dash-bootstrap-templates` which includes a collection of 22 Plotly figure templates customized
for Bootstrap themes.  This is based on `dash` V1.21.0 and `dash-bootstrap-components` V0.21.0 which uses
Boostrap V4 stylesheets.

Find sample usage in the `examples/` folder