{
    'name':'Deadline Reminder',
    'version':'1.0',
    'summary':'Send Emails to Reminder Deadlines',
    'sequence':51,
    'depends':['base', 'sale', 'mail','project','hr_timesheet'],
    'data':[
        'data/mail_template.xml',
        'data/ir_cron.xml',
    ],
    'installable':True,
    'application':True,
    'license':'LGPL-3'
}