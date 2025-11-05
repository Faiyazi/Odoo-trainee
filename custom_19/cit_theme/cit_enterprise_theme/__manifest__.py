{
    'name': 'Cit Backend Theme', 
    'summary': 'Odoo Enterprise Backend Theme',
    'version': '1.0',
    'depends': [
        'cit_appsbar',
        'cit_colors',
    ],
    'data': [
        'views/res_config_settings.xml',
    ],
    'assets': {
        'web._assets_primary_variables': [
            (
                'before', 
                'cit_colors/static/src/scss/colors.scss',
                'cit_enterprise_theme/static/src/scss/colors_light.scss'
            ),
            (
                'after', 
                'web/static/src/scss/primary_variables.scss', 
                'cit_enterprise_theme/static/src/scss/variables.scss'
            ),
        ],
        'web.assets_backend': [
            'cit_enterprise_theme/static/src/webclient/**/*.xml',
            'cit_enterprise_theme/static/src/webclient/**/*.js',
            'cit_enterprise_theme/static/src/views/**/*.scss',
            ('remove', 'cit_enterprise_theme/static/src/**/*.dark.scss'),
        ],
        "web.assets_web_dark": [
            (
                'after', 
                'cit_colors/static/src/scss/colors.scss',
                'cit_enterprise_theme/static/src/scss/colors_dark.scss'
            ),
            'cit_enterprise_theme/static/src/**/*.dark.scss',
        ],
    },
    'installable': True,
    'application': False,
    'license': 'LGPL-3',
}
