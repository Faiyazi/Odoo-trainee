{
    'name': 'Hotel Managements System',
    'version': '1.0',
    'summary': 'Hotel Managements for booking',
    'license': 'LGPL-3',
    'category': 'App',
    'depends': ['base', 'mail'],
    'data': [
        'security/ir.model.access.csv',
        'views/hotels_name_list_view.xml',
        'views/hotel_rooms_view.xml',
        'views/hotel_reservation_view.xml',
        'views/menus.xml',
    ],
    'auto_install': False,
    'application': True,
    'installable':True
}