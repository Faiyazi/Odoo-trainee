{
<<<<<<< HEAD
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
=======
    'name':'Project Team Member',
    'version': '1.0',
    'summary':'Project team',
    'sequence': 50,
    'depends':['base','hr_timesheet','mail','project'],
    'data':[
        'security/ir.model.access.csv',
        'security/project_task_rules.xml',
        'views/project_team_member_views.xml',
        'views/res_state_city_views.xml',
        "views/hr_timesheet_views.xml",
        'views/project_team_views.xml',
        'views/add_member_wizard_views.xml',
        'data/add_member_server_action.xml',
        'views/project_project_inherit_view.xml',
        'views/project_task_inherit_view.xml',
        'views/project_task_search_inherit.xml',
        'views/set_task_priority_view.xml',
        'views/menus.xml',
        'data/project_team_sequence.xml',
        'data/set_task_priority_server_action.xml',
    ],
    'demo':[
        'demo/demo_data.xml',
        'demo/project_team_member.xml',
    ],
    'installable':True,
    'application':True,
    'license': 'LGPL-3'
}
>>>>>>> ronak
