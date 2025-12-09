{
    "name": "Bell message",
    "version": "1.0",
    "description": "This is module for show last five message.",
    "license": "LGPL-3",
    "website": "https://www.example.com",
    "author": "John Doe",
    "depends": ["base","mail"],
    "installable": True,
    "application": True,
    "sequence": 1,

    "data": [
        'security/ir.model.access.csv',
        'views/bell_msg_views.xml',
       'views/bell_menu.xml',
    ],

    "assets": {
        "web.assets_backend": [
            "bell_message/static/src/js/bell_message.js",
            "bell_message/static/src/xml/bell_message.xml"
        ],
    },
}
