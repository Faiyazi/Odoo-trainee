<<<<<<< HEAD
<<<<<<< HEAD
{
    'name': 'Project Task Timesheet Reports',
    'version': '1.0',
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
=======
=======
>>>>>>> chirag
# -*- coding: utf-8 -*-
{
    'name': "Project Task Timesheet Report",
    'summary': "Short (1 phrase/line) summary of the module's purpose",
    'description': """Long description of module's purpose""",
    'author': "My Company",
    'website': "https://www.yourcompany.com",
    'category': 'Uncategorized',
    'version': '0.1',
    'depends': ['base', 'project', 'hr_timesheet'],
    'data': [
        'security/ir.model.access.csv',
        'reports/task_timesheet_template.xml',
        'views/report_wizard_views.xml',
    ],
    'license':'LGPL-3',
}

<<<<<<< HEAD
>>>>>>> chirag
=======
>>>>>>> chirag
