# -*- coding: utf-8 -*-
{
    'name': "Odoo Task-2",

    'summary': "Short (1 phrase/line) summary of the module's purpose",
    'description': """Long description of module's purpose""",
    'author': "My Company",
    'website': "https://www.yourcompany.com",
    'category': 'Uncategorized',
    'version': '0.1',
    'depends': ['base','contacts'],
    'data': [
        'security/ir.model.access.csv',
        'views/new_object_views.xml',
        'views/res_partner_inherit_views.xml',
    ],
    'license':'LGPL-3',

}

