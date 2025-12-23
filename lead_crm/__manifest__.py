{
    'name': 'crm_lead',
    'description': 'CRM Lead Management',
    'sequence': 2,
    'license': 'LGPL-3',
    'author':'Mr Destroyer',
    'application': True,
    'depends': [
        # 'project',
        'mail', 
        'base',
        'sale_management',
       
        'crm',
        'website',
    ],
    'data': [
        'views/website_menu.xml',
        'views/templates.xml',  # your crm_leads_template qweb
        
    ],
}
