from odoo import models, fields

class TestsModel(models.Model):
    _name = 'tests.model'
    _inherit = 'test.model'

    name = fields.Char(string="Name")
    age = fields.Integer(string="Age")
    