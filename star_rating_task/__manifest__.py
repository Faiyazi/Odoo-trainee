{
    'name' : "Star Rating Task",
    'version' : "1.0",
    'summary': "Star Rating Widget Implementation",
    'license': "LGPL-3",
    'description': """
        This module adds a star rating widget to the res.partner form view.
    """,    
    'sequence': 1,
    'category': "Tools",
    'author': "Black box",
    'website': "https://odoo.com",
    'depends' : ['base', 'web', 'contacts'],
    'data':[
        'views/star_rating_view.xml',
    ],
    'auto_install': False,
    'application': True,
    'installable': True,
    
    'assets': {
        'web.assets_backend': [
            "star_rating_task/static/src/js/test_star_rating.js",
            'star_rating_task/static/src/js/star_rating_js.js',
            'star_rating_task/static/src/xml/star_rating_xml.xml',
        ],
    },
}