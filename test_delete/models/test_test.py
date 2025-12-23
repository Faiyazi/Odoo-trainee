from odoo import models, fields

class TestDelete(models.Model):
    _name = 'test.delete'
    _description ='Test Delete'

    test_one = fields.One2many(
        'test.delete.test',
        'parent_id',
        string="Test Lines"
    )
