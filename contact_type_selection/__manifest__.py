# -*- coding: utf-8 -*-
{
    "name": "Contact Selection View",
    "version": "1.0",
    "license": "LGPL-3",
    "description": """
        This module demonstrates a Conatct type2 field component in Odoo 18.
        It shows a list with type2 field which change image .
    """,
    
    "sequence": 1,
    "category": "Tools",
    "author": "Black box",
    "website": "https://odoo.com",
    "depends": ["base","contacts"],
    "data": [
        "views/contact_form_selection.xml",
    ],
    
    "installable": True,
    "application": True,
    "auto_install": False,
}
