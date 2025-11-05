{
    'name': 'OWL Tutorial',
    'version': '1.0',
    'description': """OWL Tutorial""",
    'summary': 'OWL Tutorial ',
    'category': 'OWL',
    'depends': ['base', 'web'],
    'data': [
        'security/ir.model.access.csv',
        'views/todo_list_view.xml',
    ],
    'demo': [],
    'assets': {
        'web.assets_backend':[
            'owl_todo_app/static/src/components/todo_list/todo_list.js',
            'owl_todo_app/static/src/components/todo_list/todo_list.xml',
        ],
    },
    'auto_install': True,
    'application': True,
    'license': 'LGPL-3',
}