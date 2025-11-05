{
    'name': 'Cit Colors', 
    'summary': 'Customize your Odoo colors',
    'version': '1.0',
    'license': 'LGPL-3', 
    'depends': [
        'web',
        'base_setup',
    ],
    'data': [
        'templates/webclient.xml',
        'views/res_config_settings.xml',
    ],
    'assets': {
        'web._assets_primary_variables': [
            ('prepend', 'cit_colors/static/src/scss/colors.scss'),
            (
                'before',
                'cit_colors/static/src/scss/colors.scss',
                'cit_colors/static/src/scss/colors_light.scss'
            ),
        ],
        'web.assets_web_dark': [
            (
                'after',
                'cit_colors/static/src/scss/colors.scss',
                'cit_colors/static/src/scss/colors_dark.scss'
            ),
        ],
    },
    'installable': True,
    'application': False,
}
