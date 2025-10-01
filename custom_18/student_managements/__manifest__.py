{
    'name':'Student Managements',
    'version': '18.0.1.0',
    'category':'Education',
    'depends':['base'],
    'data':[
        'security/ir.model.access.csv',
        'views/student_views.xml',
        'views/student_class_view.xml',
        'data/student_sequence.xml',
    ],
    'demo':[
        'demo/class_data.xml',
    ],
    'installable':True,
    'application':True,
    'license': 'LGPL-3'
}