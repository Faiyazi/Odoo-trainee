# -*- coding: utf-8 -*-
{
    'name': 'OWL JS',
    'version': '1.3',
    'summary': 'Smootest way to use OWL in Odoo',
    'sequence': 1,
    'description': """
        This module only exists for owl testing purposes.
      """,
    'category': 'TEST/Testing',
    'website': 'https://www.odoo.com/app',
    'depends': ['base','sale_management','controller_test','web'],
    'data': [
      "security/ir.model.access.csv",
      'views/actions_menu.xml',
      'views/owl_js_menu.xml',
    ],
    'demo': [
      
    ],
    'installable': True,
    'application': True,
    'assets': {
        'web.assets_backend': [
            'owl_js/static/src/effects/js/owl_effects.js',
            'owl_js/static/src/component/js/owl_js.js',
            'owl_js/static/src/component/xml/owl_js.xml',
            # 'custom_addons/owl_js/static/src/css/owl_js_css.css',
        ],
    },
    'license': 'LGPL-3',
    
    "image":"owl_js/static/description/icon.png",
    
}
