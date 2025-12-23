{
    'name': 'sale_order_excel',
    'description': 'Sale Order Excel',
    'author':'unknown',
    'sequence': 1,
    'license': 'LGPL-3',
    'application': True,
    'depends': ['sale_management','base'],
    'data':[
        'security/ir.model.access.csv',
        'wizard/sale_order_excel.xml',
    ]
}
