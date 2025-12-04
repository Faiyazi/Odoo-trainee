{
    'name': 'Sales Functional Learning',
    'version': '1.0',
    'sequence':1,
    'summary': 'Sales Module functional learning and understand how they work.',
    'category': 'Sales',
    'depends': ['base', 'sale_management', 'stock'],
    'data': [
        'views/sale_order_inherit_view.xml',
    ],
    'auto_install': True,
    'application': True,
    'installable': True,
    'license': 'LGPL-3',
}