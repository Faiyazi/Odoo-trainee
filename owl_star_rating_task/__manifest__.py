# -*- coding: utf-8 -*-
##############################################################################
#
# Part of Caret IT Solutions Pvt. Ltd. (Website: www.caretit.com).
# See LICENSE file for full copyright and licensing details.
#
##############################################################################

{
    'name': 'OWL Start Rating',
    'summary': 'Rate partner with star widget',
    'description': '''This module contains code for start rating task using OWL JS''',
    'version': '10.0',
    'author': 'Caret It Solutions PVT. LTD.',
    'website': 'https://caretit.com',
    'depends': ["base"],
    "installable": True,
    "application": True,
    'data': [
        "views/res_partner_views.xml",
    ],
    'license': 'LGPL-3',
    'images': ['static/description/icon.png'],
    "assets": {
        "web.assets_backend": [
            # ✅ Bootstrap & Font Awesome
            "https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css",
            "https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js",
            'https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.1/font/bootstrap-icons.css',
            "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css",

            # Owl JS & XML files
            "owl_star_rating_task/static/src/js/*.js",
            "owl_star_rating_task/static/src/xml/*.xml",
        ],
    },
}
