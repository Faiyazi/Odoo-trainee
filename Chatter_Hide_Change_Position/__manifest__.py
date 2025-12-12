{
    "name": "Chatter Hide & Change Position",
    "version": "1.0",
    "description": "This Chatter is use for Hide and Change position",
    "license": "LGPL-3",
    "website": "https://www.example.com",
    "author": "John Doe",
    "depends": ["base","mail","web"],
    "installable": True,
    "application": True,
    "sequence": 1,

    "data": [
    ],

    "assets": {
        "web.assets_backend": [
            
            
            'Chatter_Hide_Change_Position/static/src/xml/hide_chatter.xml',
            'Chatter_Hide_Change_Position/static/src/xml/show_chatter.xml',
            'Chatter_Hide_Change_Position/static/src/xml/change_position.xml',

            'Chatter_Hide_Change_Position/static/src/js/chatter_hide_show.js', 
            'Chatter_Hide_Change_Position/static/src/js/chatter_change_position.js',
    
        ],
    },
}
