{
    'name': 'sale_order_excel',
    'description': 'Sale Order Excel',
    'sequence': 1,
    'license': 'LGPL-3',
    'application': True,
    'depends': ['sale_management','base'],
    'data':[
        'wizard/sale_order_excel.xml',
        # 'views/view_sale_order.xml',
    ]
}
