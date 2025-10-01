# -*- coding: utf-8 -*-
##############################################################################
#                                                                            #
# Part of Caret IT Solutions Pvt. Ltd. (Website: www.caretit.com).           #
# See LICENSE file for full copyright and licensing details.                 #
#                                                                            #
##############################################################################

{
    'name': "Delivery Process Custom",
    'summary': "Delivery Process Custom",
    'description': """Delivery Process Custom""",
    'author': 'Caret IT Solutions Pvt. Ltd.',
    'website': 'http://www.caretit.com',
    'category': 'Inventory',
    'version': '18.0.1.0',
    'depends': ['base', 'sale_management', 'stock', 'session_company'],
    'data': [
        'security/ir.model.access.csv',
        'report/report_deliveryslip.xml',
        'views/delivery_location_area_view.xml',
        'views/delivery_truck_view.xml',
        'views/res_partner_views.xml',
        'views/sale_order_views.xml',
        'views/stock_picking_views.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': False,
    'license':'LGPL-3'
}
