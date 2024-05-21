window.dash_clientside = window.dash_clientside || {};

window.dash_clientside.themeSwitch = {

    applyDbcClass: function (_) {
        let dash_container = document.querySelector('#_dash-app-content')

        // create a set with existing classes (if there are)
        let classNameSet = new Set(dash_container.className.split(" "))
        // add the dbc class if not already in the set
        classNameSet.add('dbc')
        // set the container className
        dash_container.className = [...classNameSet].join(' ').trim()
        return window.dash_clientside.no_update
    },


    toggleTheme: function (switchOn, themes) {

        /**
         * Clean if there are several themes stylesheets applied
         * or create one if no stylesheet is found.
         * @param {array} `themes` - List of themes url to search
         * @returns {HTMLElement} - Return a stylesheet that can be used for the theme to be applied
         */
        const cleanedStylesheets = function (themes) {
            // find the stylesheets
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
            return stylesheet
        }

        // if only one theme provided (using a string): use the color mode
        if (typeof themes === "string") {
            const theme = themes
            stylesheet = cleanedStylesheets([theme]) // return the stylesheet to use after cleaning
            stylesheet.setAttribute('href', theme) // to be sure to have the right stylesheet
            // toggle between light and dark theme using color mode
            document.documentElement.setAttribute('data-bs-theme', switchOn ? 'light' : 'dark')
        } else {
            let [currentTheme, newTheme] = switchOn ? themes : themes.toReversed()
            stylesheet = cleanedStylesheets(themes) // return the stylesheet to use after cleaning
            // update the theme
            stylesheet.setAttribute('href', newTheme)
        }

        return window.dash_clientside.no_update
    }
}
