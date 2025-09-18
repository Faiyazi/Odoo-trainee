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