# -*- coding: utf-8 -*-
##############################################################################
#                                                                            #
# Part of Caret IT Solutions Pvt. Ltd. (Website: www.caretit.com).           #
# See LICENSE file for full copyright and licensing details.                 #
#                                                                            #
##############################################################################
{
    'name': 'Auto Field Color',
    'summary': 'Custom field widget to show fields with dynamic background colors',
    'category': 'web',
    'depends': ['web'],
    'description': """
        This module introduces a dynamic color display widget for Odoo fields,
            allowing developers to visually highlight data values in form and list views.

        **Key Features:**
        - Adds a reusable `auto_field_color` widget for supported field list following.
          'char', 'text', 'integer', 'float', 'date', 'datetime',
          'monetary', 'boolean', 'many2one', 'selection'.
        - Supports custom background colors using the XML `options` attribute.
        - If no `options` are provided, the widget defaults to a grey background color.

        **Color Feature:**
        - To display a custom color in a field, use the `widget` and `options` attribute in the 
        XML column definition:-
        
        <field name="price_unit" widget="auto_field_color" options="{'color': 'green'}"/>
        
        **Notes:**
        - This widget does not support the following field types:
        -    'one2many', 'many2many', 'image', 'binary'.
    """,
    'author': 'Caret IT Solutions Pvt. Ltd.',
    'website': 'https://www.caretit.com/',
    'data':[],
    'assets': {
        'web.assets_backend': [
            'cit_auto_field_color/static/src/js/auto_field_color.js',
            'cit_auto_field_color/static/src/xml/auto_field_color.xml',
        ],
    },
    'auto_install': False,
    'license': 'LGPL-3',
}