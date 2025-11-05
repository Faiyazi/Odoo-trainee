{
    'name': 'Cit AppsBar', 
    'summary': 'Adds a sidebar to the main screen',
    'version': '1.0',
    'depends': [
        'base_setup',
        'web',
    ],
    'data': [
        'templates/webclient.xml',
        # 'views/res_users.xml',
    ],
    'assets': {
        'web._assets_primary_variables': [
            'cit_appsbar/static/src/scss/variables.scss',
        ],
        'web._assets_backend_helpers': [
            'cit_appsbar/static/src/scss/mixins.scss',
        ],
        'web.assets_web_dark': [
            (
                'after',
                'cit_appsbar/static/src/scss/variables.scss',
                'cit_appsbar/static/src/scss/variables.dark.scss',
            ),
        ],
        'web.assets_backend': [
            (
                'after',
                'web/static/src/webclient/webclient.js',
                'cit_appsbar/static/src/webclient/webclient.js',
            ),
            (
                'after',
                'web/static/src/webclient/webclient.xml',
                'cit_appsbar/static/src/webclient/webclient.xml',
            ),
            (
                'after',
                'web/static/src/webclient/webclient.js',
                'cit_appsbar/static/src/webclient/menus/app_menu_service.js',
            ),
            (
                'after',
                'web/static/src/webclient/webclient.js',
                'cit_appsbar/static/src/webclient/appsbar/appsbar.js',
            ),
            'cit_appsbar/static/src/webclient/webclient.scss',
            'cit_appsbar/static/src/webclient/appsbar/appsbar.xml',
            'cit_appsbar/static/src/webclient/appsbar/appsbar.scss',
        ],
    },
    'installable': True,
    'application': False,
    'license': 'LGPL-3',
}
