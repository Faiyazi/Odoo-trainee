from odoo import models, fields


class TestModel(models.AbstractModel):
    _name = 'test.model'
    _description = 'Test Model'


    test_field = fields.Char(string='Test Field')