{
    'name': 'Timesheet',
    'version': '1.0',
    'summary': 'Custom Timesheet Management',
    'description': 'Simple custom module to understand Odoo module structure',

    'category': 'Productivity',
    'depends': ['base'],
    'data': [
        "security/ir.model.access.csv",
        "views/timesheet_task_views.xml",
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
