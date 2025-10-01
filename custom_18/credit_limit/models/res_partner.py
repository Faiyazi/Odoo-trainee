from odoo import fields, models

class ResPartner(models.Model):
    _inherit = 'res.partner'

    partner_credit_limit = fields.Float(string="Partner Credit Limit ")
