{
    'name': 'Sale Order Wizard',
    'version': '1.0',
    'description': '',
    'summary': 'Sale Order Import Wizard with Excel Upload.',
    'depends': ['base', 'sale_management'],
    'data': [
        'security/ir.model.access.csv',
        'views/sale_order_inherit_view.xml',
        'wizard/sale_order_wizard_view.xml',
    ],
    'auto_install': False,
    'application': True,
    'installable':True,
    'license': 'LGPL-3',
}