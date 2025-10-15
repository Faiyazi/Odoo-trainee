{
    "name": "OWL Todo App",
    "version": "1.0",
    "summary": "Simple ToDo App using Owl JS in Odoo 18",
    "depends": ["web"],
    "data": [
        'security/ir.model.access.csv',
        'views/todo_list_views.xml',
    ],
    "assets": {
        "web.assets_backend": [
            "owl_todo/static/src/components/**/*.xml",

            "owl_todo/static/src/components/**/*.js",

            "owl_todo/static/src/components/todo_list/todo_list.scss",
        ],
    },
    "license": "LGPL-3",
    "installable": True
}