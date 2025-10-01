{
    'name':'Project Team',
    'description':'Project team member module ',
    'author': 'Chirag Bharada',
    'website': 'https://www.odoo.com',
    'depends': ['base','analytic','mail','project','hr_timesheet','hr_skills',],
    'license': 'LGPL-3',
    'data': [
        'security/ir.model.access.csv',
        'data/seq_project_team.xml',
        'views/project_menu.xml',
        'views/project_team_member_views.xml',
        'views/project_task_inherit_assign_date_views.xml',
        'views/project_project_views.xml',
        'views/project_team_views.xml',
        'views/project_task_inherit_priority_views.xml',
        'views/hr_timesheet_inherit_views.xml',
        'views/rec_city_demo_views.xml',
        'views/alphabetically_task_views.xml',
        'wizard/add_member_wizard_views.xml',
    ],
    'demo':[
        'demo/rec_city_demo.xml',
        'demo/project_team_member_demo.xml',

    ],
    'installable': True,
    'auto_install': False,
}
