{
    "name": "Test Controller",
    "description": "Owl JS module for practice.",
    "license": "LGPL-3",
    "website": "www.example.com",
    "author": "John Doe",
    "depends": ["base","web","website","contacts"],
    "installable" : True,
    "application" : True,
    "sequence" : 1,
    "data": [
        "security/ir.model.access.csv",
        "views/template_controller.xml",
        "views/testcontrollerviews.xml",
        "views/testcontrolleractions.xml",
        "views/testcontrollermenu.xml",
        "views/test_template.xml",
        
        ],
    "assets": {
         'web.assets_frontend': [
            'controller_test/static/src/css/test_controller.css',
        ],
   
        },
}