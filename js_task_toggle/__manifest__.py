{
    'name' : 'Toggle button',
    'description': """This module is use for toggle 
                    inside the Contact form.
                    """,
    "license": "LGPL-3",
    'sequence' : 1,
    'author' : 'MR Destroyer',
    'depends' : ["base","contacts"],
    'data' : [
        'views/res_partner_toggle.xml',
        ],
    "installable": True,
    "application": True,
    'assets': {
    'web.assets_backend': [
        'js_task_toggle/static/src/js/toggle_button.js',
        'js_task_toggle/static/src/xml/toggle_button.xml',
    ],
},

                    
}