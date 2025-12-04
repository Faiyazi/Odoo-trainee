# -*- coding: utf-8 -*-
##############################################################################
#                                                                            #
# Part of Caret IT Solutions Pvt. Ltd. (Website: www.caretit.com).           #
# See LICENSE file for full copyright and licensing details.                 #
#                                                                            #
##############################################################################

{
    'name': 'Session Company',
    'version': '1.1',
    'category': 'Company',
    'summary': 'Session Company',
    'description': """
        This module will add the field for session company to required models.
    """,
    'author': 'Caret IT Solutions Pvt. Ltd.',
    'website': 'https://www.caretit.com',
    'depends': ['base','sale','product','stock', 'hr', 'sale_stock'],
    'data': [
        'views/partner_view.xml',
        'views/product_pricelist_views.xml',
        'views/sale_order_view.xml',
        'views/stock_picking_view.xml',
        'views/res_config_settings_views.xml',
        'views/hr_employee_views.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application':True,
    'license': 'LGPL-3',
}
