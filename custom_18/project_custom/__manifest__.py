<<<<<<< HEAD
# -*- coding: utf-8 -*-
{
    'name': "Project Custom",
    'summary': "Short (1 phrase/line) summary of the module's purpose",
    'description': """Long description of module's purpose""",
    'author': "chirag Bharada",
    'website': "https://www.yourcompany.com",
    'category': 'Uncategorized',
    'license': 'LGPL-3',
    'version': '0.1',
    'depends': ['base','project','startend_mixin','report_xlsx'],

     'data': [
        'security/ir.model.access.csv',
        # "'views/project_task_inherit_views.xml',
            'wizards/project_task_report_views.xml',
            'reports/report_template.xml',

     ],

    'installable': True,
    'application': True,

}

=======
{
    'name':'Project Custom',
    'version':'18.0.1.0',
    'summary':'project custom module',
    'sequence':45,
    'depends':['base','project', 'startend_mixin', 'report_xlsx'],
    'data':[
        'security/ir.model.access.csv',
        'views/project_task_inherit_view.xml',
        'views/export_task_wizard_view.xml',
        'views/project_task_view.xml',
        'views/menus.xml',
        'reports/pdf_template.xml',
        'reports/ir_action_report.xml',
    ],
    'installable':True,
    'application':True,
    'license':'LGPL-3'
}
>>>>>>> ronak
