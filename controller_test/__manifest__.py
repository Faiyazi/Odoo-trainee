{
    "name": "Test Controller",
    "version": "1.0",
    "description": "Owl JS module for practice.",
    "license": "LGPL-3",
    "website": "https://www.example.com",
    "author": "John Doe",
    "depends": ["base", "web", "website", "contacts", "mail"],
    "installable": True,
    "application": True,
    "sequence": 1,

    "data": [
        "security/ir.model.access.csv",
        "data/mail_template_test.xml",
        "report/controller_test_report.xml",
        "views/template_controller.xml",
        "views/testcontrollerviews.xml",
        "views/testcontrolleractions.xml",
        "views/testcontrollermenu.xml",
        "views/test_template.xml",
    ],

    "assets": {
        "web.assets_frontend": [
            "controller_test/static/src/css/test_controller.css",
        ],
    },
}
