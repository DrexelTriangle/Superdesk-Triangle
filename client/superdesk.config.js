/**
 * This is the default configuration file for the Superdesk application. By default,
 * the app will use the file with the name "superdesk.config.js" found in the current
 * working directory, but other files may also be specified using relative paths with
 * the SUPERDESK_CONFIG environment variable or the grunt --config flag.
 */
module.exports = function(grunt) {
    return {
        defaultRoute: '/workspace/personal',

        server: {
            url: 'http://localhost/api',
            ws: 'ws://localhost/ws'
        },

        view: {
            timeformat: 'HH:mm',
            dateformat: 'MM.DD.YYYY'
        },

        features: {
            preview: 1,
            swimlane: {columnsLimit: 4},
            noTakes: true,
            editor3: true,
            validatePointOfInterestForImages: false,
            editorHighlights: true,
            noPublishOnAuthoringDesk: true,
            noMissingLink: true
        },

        list: {
            'priority': [],
            'firstLine': [
                'headline'
            ],
            'secondLine': [
                'state',
                'embargo',
                'update',
                'expiry'
            ]
        }
    };
};