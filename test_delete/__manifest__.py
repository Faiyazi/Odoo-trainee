# -*- coding: utf-8 -*-
##############################################################################
#                                                                            #
# Part of Caret IT Solutions Pvt. Ltd. (Website: www.caretit.com).           #
# See LICENSE file for full copyright and licensing details.                 #
#                                                                            #
##############################################################################

{
    'name': 'Test Detele',
    'summary': 'Delete configuration',
    'description':
        """ 
         Delete configuration
        """,
    'version': '19.0.1.0',
    'category': 'Administration',
    'author': 'Caret IT Solutions Pvt. Ltd.',
    'website': 'https://www.caretit.com',
    'support': 'sales@caretit.com',
    'license': 'LGPL-3',
    'depends': [],
    'data': [
        'security/ir.model.access.csv',
        'views/test_delete_test.xml',
        'views/test_delete.xml',
        'views/test_menu.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': False,
    
     "assets": {
        "web.assets_backend": [
            'test_delete/static/src/xml/test_delete_test_web.xml',
        ],},
    
}
