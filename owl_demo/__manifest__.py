# -*- coding: utf-8 -*-
{
    "name": "OWL Demo Component",
    "version": "1.0",
    "summary": "Demo of Odoo 18 OWL component",
    "license": "LGPL-3",
    "description": """
        This module demonstrates a simple OWL 2.x component in Odoo 18.
        It shows a list with add-item functionality using OWL reactive state.
    """,
    "category": "Tools",
    "author": "Your Name",
    "website": "https://yourwebsite.com",
    "depends": ["base", "web"],
    "data": [
        "views/demo_action.xml",
    ],
    "assets": {
        "web.assets_backend": [
            "owl_demo/static/src/js/demo_component.js",
            "owl_demo/static/src/xml/demo_template.xml",
            
        ],
    },
    "installable": True,
    "application": True,
    "auto_install": False,
}
