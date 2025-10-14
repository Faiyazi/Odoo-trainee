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

