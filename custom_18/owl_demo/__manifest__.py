{
<<<<<<< HEAD
    'name': 'OWL Demo',
    'summary': 'Basic OWL Component Example',
    'category': 'Learning',
    'version': '1.0',
    'depends': ['web'],
    'data': [
        'views/owl_demo_action.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'owl_demo/static/src/js/owl_demo.js',
            'owl_demo/static/src/js/owl_demo_template.xml'
        ],
    },
    'installable': True,
    'application': False,   
=======
    "name": "Owl Demo",
    "version": "1.0",
    "summary": "Simple Hello World using Owl JS in Odoo 18",
    "depends": ["web"],
    "data": [
        "views/hello_world_menu.xml"
    ],
    "assets": {
        "web.assets_backend": [
            "owl_demo/static/src/xml/counter_template.xml",
            "owl_demo/static/src/js/counter.js",
        ],
    },
    "license": "LGPL-3",
    "installable": True
>>>>>>> chirag
}