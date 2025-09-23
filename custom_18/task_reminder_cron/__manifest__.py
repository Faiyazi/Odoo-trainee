# -*- coding: utf-8 -*-
{
    'name': "Task Reminder",
    'summary': "Task Reminders & Timesheet Entry Send",
    'description': """Long description of module's purpose""",
    'author': "My Company",
    'website': "https://www.yourcompany.com",
    'category': 'Uncategorized',
    'version': '0.1',
    'depends': ['hr_timesheet','project','mail'],
    'license':'LGPL-3',
    'data': [
        'security/ir.model.access.csv',
        'data/cron_job.xml',
        'data/task_email_template.xml',
        'data/timesheet_email_template.xml',
    ],
    'installable': True,
    'application': True,
}

