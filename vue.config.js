const path = require('path')
const PrerenderSPAPlugin = require('prerender-spa-plugin')

module.exports = {
    configureWebpack: () => {
        if (process.env.NODE_ENV !== 'production') return;
        return {
            plugins: [
                new PrerenderSPAPlugin(
                    // absolute path to compiled SPA
                    path.resolve(__dirname, 'dist'),
                    // list of routes to prerender
                    [ '/'],
                    {
                        // options
                    }
                ),
            ]
        }
    }
}