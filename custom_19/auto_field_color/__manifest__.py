{
    'name': "Auto Field Color",
    'version': '1.0',
    'author': "MyCompany",
    'license': "LGPL-3",
    'depends': ['web'],
    'summary': "Custom field widget to show fields with dynamic background colors",
    'description': """
            This module adds a reusable Odoo widget that allows you to display field values
with automatically styled background colors.""",
    'assets': {
        'web.assets_backend': [
            'auto_field_color/static/src/xml/auto_field_color_templates.xml',
            'auto_field_color/static/src/js/auto_field_color.js',
            'auto_field_color/static/src/css/auto_field_color.css',
        ],
    },
    'installable': True,
    'application': False,
}
