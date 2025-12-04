{
    'name': 'College ERP',
    'version': '1.2',
    'summary': 'Manage Students, Teachers, Attendance, and Exams',
    'description': 'A Complete Module To Manage College Operations',
    'author': 'Chirag Bharada',
    'website': 'https://www.odoo.com',
    'category': 'Education',
    'sequence': 1,
    'depends': ['base', 'mail', 'web'],
    'license': 'LGPL-3',
    'data': [
    'security/college_erp_security.xml',
    'security/ir.model.access.csv',
    'security/college_erp_record_rules.xml',
    'data/cron_birthday.xml',
    'data/student_sequence.xml',
    'data/mail_template_data.xml',
    'wizard/admission_wizard_view.xml',
    'views/college_student_admission_views.xml',
    'views/college_teacher_views.xml',
    'views/college_staff_views.xml',
    'views/college_menu.xml',
    'report/report_template.xml',

    ],
    'demo':[
        'demo/teacher_demo.xml',
        'demo/college.teacher.csv',

    ],
    'installable': True,
    'application': True,
    'auto_install': False,

}

