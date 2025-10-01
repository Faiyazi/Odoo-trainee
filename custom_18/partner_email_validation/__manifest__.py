{
    'name':'Email Validation',
    'version':'18.0.1.0',
    'summary':'Email Validation on res.partner and uniqueness',
    'sequence':50,
    'depends':['base', 'mail', 'sale_management'],
    'data':[
        'views/res_partner_view.xml',
    ],
    'installable':True,
    'application':True,
    'license':'LGPL-3'
}