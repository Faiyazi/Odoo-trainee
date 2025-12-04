{
    'name': 'project_team',
    'description': 'Project Team',
    'sequence': '1',
    'application': True,
    'installable': True,
    'license': 'LGPL-3',
    'depends': ['base', 'project', 'account', 'mail', 'hr_timesheet','owl_js'],
    'data': [
        # 'security/security.xml',
        'security/ir.model.access.csv',
        'data/sequence.xml',
        'data/data_records_team_member.xml',
        # 'demo/demo_date.xml',
        'data/data_res_state_city.xml',
        'wizard/project_team_wizard.xml',
        'views/project_team_view.xml',
        'views/team_members_view.xml',
        'views/timesheet.xml',
        'views/project_project_inherit.xml',
        'views/project_team_member_views.xml',
        'views/project_team_member_menu.xml',
    ],
    'image': [
        'static/description/icon.png'
    ],
    'assets': {
        'web.assets_backend': [
            'project_team/static/src/css/custom_project_team.css',
        ],
    },
}
