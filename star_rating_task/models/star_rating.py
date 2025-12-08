from odoo import models, fields


class StarRating(models.Model):
    _inherit = 'res.partner'

    record_rating = fields.Float(string="Star Rating")