{
    'name': 'task_remainder',
    'description': 'Task Remainder',
    'sequence': 2,
    'license': 'LGPL-3',
    'application': True,
    'depends': [
        # 'project',
        'mail',
        'base',
        'sale_management',
        'contacts',
        'purchase',
        'crm',
        'website',
    ],
    'data': [
        'views/task_remainder.xml',
        'data/data_task_remainder.xml',
        'data/email_remainder.xml',
        
    ],
}
