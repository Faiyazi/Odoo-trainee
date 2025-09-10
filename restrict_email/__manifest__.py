{
    'name': 'restrict_mail',
    'description': 'Restrict mail',
    'version': '1.3',
    'author': 'Annoynse',
    'sequence': '1',
    'application':True,
    'depends':['base','sale','mail'],
    'data':[
        'views/view_restricted_partner.xml',
    ],
    'license': 'LGPL-3',

}