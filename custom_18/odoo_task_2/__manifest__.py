{
    'name': 'Contact Custom Category',
    'version': '1.0',
    'summary': 'Add custom category field to contacts and ensure case-insensitive imports.',
    'category': 'Contacts',
    'depends': ['base', 'contacts'],
    'data': [
        "security/ir.model.access.csv",
        'views/res_partner_custom_views.xml',
    ],
    'installable': True,
    'application': False,
}
