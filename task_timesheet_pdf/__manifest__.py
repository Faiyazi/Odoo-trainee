{
    'name':'task_timesheet_pdf',
    'description':'Task  TimeSheet',
    'sequence':2,
    'license': 'LGPL-3',
    'application': True,
    'depends':['project_custom','project'],
    'data':[
      'security/ir.model.access.csv',
      'wizard/task_timesheet_pdf.xml',
      'report/task_timesheet_report.xml'
    ],
    'installable': True,
}