{
    'name': 'Sale Order Excel Import',
    'version': '1.2',
    'summary': 'Import Sale Order Lines from Excel via Wizard',
    'category':'Sales',
    'depends': ['sale',],
    'license': 'LGPL-3',
    'data': [
        'security/ir.model.access.csv',
        'views/sale_order_view.xml',
        'views/sale_order_wizard_view.xml',
    ],
    'installable': True,
    'auto_install': False,

}