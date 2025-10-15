{
    'name': 'Customer PDF Report',
    'version': '1.0',
    'summary': 'Generate a simple PDF that lists customers.',
    'license': 'LGPL-3',
    'depends': ['base', 'contacts'],
    'data': [
        'reports/pdf_template.xml',
        'reports/report.xml',
        'views/menus_view.xml',
    ],
    'auto_install': False,
    'application': True,
    'installable':True
}