{
    'name': 'Contact Credit Management',
    'version': '1.0',
    'category': 'contacts',
    'summary': 'Contact Credit Management',
    'description': """
        This module providing the credit management for contacts.
        1) Contact:
            > Total credit limit can be manually set over contact,
            > You will be able to see Total open account value,
            > Based on these you will be able to see the currect credit limit,
            > You will also be able to see the total overdue credit. 
        2) Sale Order:
            Above mentioned all credit fields you will also be able to see on SO based on selected contact.
    """,
    'author': 'Caret IT Solutions Pvt. Ltd.',
    'website': 'https://www.caretit.com',
    'depends': ['contacts', 'sale_management', 'account', 'session_company'],
    'data': [
        # 'data/account_followup_data.xml',
        'views/partner_view.xml',
        'views/sale_order_view.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application':True,
    'license': 'LGPL-3',
}