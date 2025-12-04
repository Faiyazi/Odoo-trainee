from odoo import models, fields

class TransModel(models.TransientModel):
    _name = 'trans.model'
    _description = 'Trans Model'


    name1 = fields.Char(string='Name')
    phone = fields.Integer(string='Mobile')

    def action_open_wizard(self):
        pass