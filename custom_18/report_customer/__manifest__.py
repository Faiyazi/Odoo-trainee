{
    'name': 'report_customer',
    'description': 'Report Customer',
    'version': '1.3',
    'author': 'Annoynse',
    'sequence': '1',
    'application': True,
    'depends': ['base', 'mail', 'contacts'],
    'data': [
        'security/ir.model.access.csv',
        'report/resport_customer_pdf.xml',
        'views/view_report_customer.xml',
    ],

    # 'assets': {
    #     'web.report_assets_pdf': [
    #         '/home/hp/odoo18/custom_addons/report_customer/wizard/reeport_customer.py'
    #     ],
    # },
    'license': 'LGPL-3',
}
