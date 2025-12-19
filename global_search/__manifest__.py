{
    'name' : 'Global Search',
    'description': """This module is use for toggle 
                    inside the Contact List view.
                    """,
    "license": "LGPL-3",
    'sequence' : 1,
    'author' : 'MR Destroyer',
    'depends' : ["base","web"],
    'data' : [
        # 'views/res_partner_toggle.xml',
        ],
    "installable": True,
    "application": True,
    'assets': {
    'web.assets_backend': [
        'global_search/static/src/js/global_search.js',
        'global_search/static/src/xml/global_search.xml',
        'global_search/static/src/css/global_search.scss',
    ],
},                  
}