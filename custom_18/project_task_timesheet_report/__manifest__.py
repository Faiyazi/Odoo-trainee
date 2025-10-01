{
    'name': 'Project Task Timesheet Reports',
    'version': '18.0.1.0',
    'summary': 'Create a complex grouped PDF report for project.task with timesheets also for selected dates.',
    'depends': ['base', 'project'],
    'data': [
        'security/ir.model.access.csv',
        'wizard/export_pdf_report_view.xml',
        'reports/pdf_report.xml',
        'reports/pdf_template.xml',
        'views/menus_view.xml',
    ],
    'auto_install': False,
    'application': True,
    'installable': True,
    'license': 'LGPL-3',
}