{
    'name': 'Email validate OWL',
    'summary': 'its validate the email id',
    'description': '''This module contains code for Email validation''',
    'version': '10.0',
    'author': 'unknown',
    'website': 'https://caretit.com',
    'depends': ["base","contacts"],
    "installable": True,
    "application": True,
    'data': [
        "views/valid_email.xml",
    ],
    'license': 'LGPL-3',
    "assets": {
        "web.assets_backend": [
      
            "owl_validate_email/static/src/js/email_validation.js",
            "owl_validate_email/static/src/xml/email_validation_template.xml",
            "owl_validate_email/static/src/js/username_field/username_field.js",
            "owl_validate_email/static/src/js/username_field/username_field.xml",
            "owl_validate_email/static/src/js/username_field/username_field.scss"
        ],
    },
}
