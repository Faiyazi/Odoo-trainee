from odoo import models, fields

class TestDeleteLine(models.Model):
    _name = 'test.delete.test'

    name = fields.Char('Name')
    parent_id = fields.Many2one(
        'test.delete',
        string="Parent",
        ondelete='cascade'  # important
    )
