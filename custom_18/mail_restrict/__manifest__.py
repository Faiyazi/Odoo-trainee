<<<<<<< HEAD
# -*- coding: utf-8 -*-
{
    'name': "Mail Restrict",
    'summary': "Short (1 phrase/line) summary of the module's purpose",
    'description': """Long description of module's purpose """,
    'author': "My Company",
    'website': "https://www.yourcompany.com",
    'category': 'Uncategorized',
    'version': '0.1',
    'license': 'LGPL-3',
    'depends': ['base','mail','sale_management'],
    'data': [
         'views/restrict_mail_views.xml',
     ],

}

=======
{
    'name': 'Email Restriction',
    'version': '18.0.1.0',
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
>>>>>>> ronak
