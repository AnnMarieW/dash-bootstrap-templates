
## 1.0.0
V1.0.0 is based on based on `dash` V2.0.0 and `dash-bootstrap-components` V1.0.0 which uses
Boostrap V5 stylesheets.

### Added
 - added "QUARTZ", "MORPH", "VAPOR", "ZEPHYR" themes
 - added 2 All-In-One components to switch themes. 
   - `ThemeSwitchAIO` toggles between two themes
   - `ThemeChangerAIO` opens a Offcanvas component to select any of the 26 themes
   - `template_from_url` helper function to get the figure template name for the selected theme
 - added `dbc.css` which minimally styles `dash-core-components` and the `DataTable` with  the selected Bootstrap theme
 - added examples of the2 AIO components that switch themes.

## Changes
 - updated `_create_templates.py` to generate figure templates based on Boostrap V5 stylesheets


## 0.1.1

This is the initial release of `dash-bootstrap-templates` which includes a collection of 22 Plotly figure templates customized
for Bootstrap themes.  This is based on `dash` V1.21.0 and `dash-bootstrap-components` V0.21.0 which uses
Boostrap V4 stylesheets.

Find sample usage in the `examples/` folder