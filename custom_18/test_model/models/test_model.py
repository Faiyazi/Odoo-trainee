from odoo import models, fields, api


class TestModel(models.Model):
    _name = 'test.model'
    _description = 'test_model.test_model'
    _inherit = 'test.model.abstract'




