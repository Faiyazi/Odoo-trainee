{
    'name':'test_custome',
    'description': 'Test Custom',
    'version': '1.3',
    'license': 'LGPL-3',
    'author': 'Annoynse',
    'summary': 'eduction,sport,free learning',
    'sequence': '1',
    'application': True,
    'installable': True,
    'depends':['project','report_xlsx','website','point_of_sale'],

    'data':[
        'security/ir.model.access.csv',
        # 'views/test_custom_web_dev.xml',
        'views/template_test_custom.xml',
        # 'views/assests.xml',
        # 'views/demo_action_test_custom.xml',
        
        
        'views/action_test_custom_view.xml',
        'views/menu_test_custom.xml',     
        'reports/report_testcustom.xml'
           
        ],
    
    'assets': {
        "web.assets_backend":['testcustom/static/src/js/test_custom_owl.js',],
        
        
        "web.assets_frontend": [
        'testcustom/static/src/css/template_test_custom.css',
    ],},
}