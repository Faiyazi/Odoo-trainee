from odoo import fields, models

class ResPartner(models.Model):
    _inherit = 'res.partner'

    record_rating = fields.Integer(string="Rating", default=0)
