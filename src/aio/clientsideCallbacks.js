window.dash_clientside = window.dash_clientside || {};

window.dash_clientside.themeSwitch = {


    toggleTheme: function (switchOn, themes, assetsUrlPath) {

        // function to test if the theme is an external or a local theme
        const isValidHttpUrl = (theme) => {
            try {
                new URL(theme);
                return true;
            } catch (error) {
                return false;
            }
        }

        // if local themes are used, modify the path to the clientside path
        themes = themes.map(theme => isValidHttpUrl(theme) ? theme : `/${assetsUrlPath}/${theme.split('/').at(-1)}`)

        // Clean if there are several themes stylesheets applied or create one if no stylesheet is found
        // Find the stylesheets
        let stylesheets = []
        for (const theme of themes) {
            stylesheets.push(...document.querySelectorAll(`link[rel='stylesheet'][href*='${theme}']`))
        }
        // keep the first stylesheet
        let stylesheet = stylesheets[0]
        // and clean if more than one stylesheet are found
        for (let i = 1; i < stylesheets.length; i++) {
            stylesheets[i].remove()
        }
        // or create a new one if no stylesheet found
        if (!stylesheet) {
            stylesheet = document.createElement("link")
            stylesheet.rel = "stylesheet"
            document.head.appendChild(stylesheet)
        }

        // Update the theme
        let newTheme = switchOn ? themes[0] : themes.toReversed()[0]
        stylesheet.setAttribute('href', newTheme)
        return window.dash_clientside.no_update
    }
}
