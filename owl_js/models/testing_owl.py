from odoo import models, fields

class TestingOwl(models.Model):
    _name = 'testing.owl'
    _description = 'Testing OWL Model'
    
    
    image = fields.Binary(string='Image')
    name = fields.Char(string='Name', required=True)
    price = fields.Float(string='Price')
    description = fields.Text(string='Description')
    
    
    def onclickbtn(self):
        return {
            'effect': {
                'fadeout': 'slow',
                'message': 'this is rainbow',
                'imag_url': '/school_student/static/src/img/sc.png',
                'type': 'rainbow_man'

            }
        }