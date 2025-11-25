# -*- coding: utf-8 -*-
##############################################################################
#                                                                            #
# Part of Caret IT Solutions Pvt. Ltd. (Website: www.caretit.com).           #
# See LICENSE file for full copyright and licensing details.                 #
#                                                                            #
##############################################################################

{
    'name': "Sale Register Report",
    'version': '1.0',
    'category': 'Reporting',
    'summary': "Generate the sale Register report",
    'description': """
        This module allows users to generate Sale Register reports in Excel format
        with detailed information on pickings, invoices, credit/debit notes, and quality checks.
    """,
    'author': 'Caret IT Solutions Pvt. Ltd.',
    'website': 'https://www.caretit.com',
    'license': 'LGPL-3',
    'depends': ['accountant', 'sale', 'stock', 'contacts','quality_control','cits_quality_extend',],
    'data': [
        'security/ir.model.access.csv',
        'views/sale_report_views.xml',
    ],
    'installable': True,
    'application': False,
}
