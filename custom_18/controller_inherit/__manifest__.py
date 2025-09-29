# -*- coding: utf-8 -*-
{
    'name': "Controller Inherit",
    'summary': "Add discounts to products and filter discounted products on the the shop page.",
    'description': """
        This module allows users to set discounts on products and providesa custom route to display only discounted products on the shop page.
        -Add a discount filed to products.
        -Filter products wih discounts on the shop page. 
    """,
    'author': "My Company",
    'website': "https://www.yourcompany.com",
    'category': 'website',
    'version': '0.1',
    'depends': ['website_sale'],
    'data': [
        'views/website_menu_views.xml',
        'views/product_views.xml',
        'views/website_sale_inherit_templates.xml',
    ],
    'application': True,
    'installable': True,
    'auto_install': False,
    'license':'LGPL-3',

}

