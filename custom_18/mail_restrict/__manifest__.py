{
    'name': 'Email Restriction',
    'version': '1.0',
    'description': 'Email restriction in chatter',
    'license': 'LGPL-3',
    'depends': ['base', 'mail', 'sale_management'],
    'data': [
        'views/res_partner_view.xml',
    ],
    'auto_install': False,
    'application': True,
    'installable':True
}