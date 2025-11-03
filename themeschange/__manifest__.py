{
    'name': 'Theme Change',
    'category': 'web/List',
    'depends': ['web'],
    'description': "This module for theme change",
    'author': 'Caret IT Solutions Pvt. Ltd.',
    'website': 'https://www.caretit.com/',
    'data': [
        'security/ir.model.access.csv',
        'views/theme_change_views.xml',
        'views/theme_change_action.xml',
        'views/theme_change_menu.xml',
        ],
    'assets': {
        'web.assets_backend': [
            'themeschange/static/src/js/theme_change.js',
            
            'themeschange/static/src/xml/theme_change_owl.xml',
        ],
    },
    'auto_install': False,
    'license': 'LGPL-3',
}
