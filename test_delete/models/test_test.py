from odoo import models, fields

class TestDelete(models.Model):
    _name = 'test.delete'

    test_one = fields.One2many(
        'test.delete.test',
        'parent_id',
        string="Test Lines"
    )
