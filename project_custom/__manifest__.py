{
    'name':'project_custom',
    'description':'Project Custom',
    'sequence':2,
    'author':'unknown',
    'license': 'LGPL-3',
    'application': True,
    'depends':['project','hr_timesheet','report_xlsx',],
    'data':[
        'security/ir.model.access.csv',
        'wizard/date_range_wizard.xml',
        'reports/date_range.xml',
        'view/project_date_range.xml'
    ],
    'installable': True,
}