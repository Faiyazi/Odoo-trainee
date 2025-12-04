# -*- coding: utf-8 -*-
{
    "name": "OWL Contact Form",
    "version": "1.0",
    "summary": "Demo of Odoo 18 OWL component",
    "license": "LGPL-3",
    "description": """
        This module demonstrates a simple OWL 2.x component in Odoo 18.
        It shows a list with add-item functionality using OWL reactive state.
    """,
    "sequence": 1,
    "category": "Tools",
    "author": "Black box",
    "website": "https://odoo.com",
    "depends": ["base", "web", "contacts"],
    "data": [
        "views/contact_form_inherit.xml",
    ],
    "assets": {
        "web.assets_backend": [
            "owl_contact_form/static/src/*/**"
            ""
            # "owl_contact_form/static/src/js/star_form.js",
            # "owl_contact_form/static/src/xml/star_field.xml",
        ],
    },
    "installable": True,
    "application": True,
    "auto_install": False,
}
