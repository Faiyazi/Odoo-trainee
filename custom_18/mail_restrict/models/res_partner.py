from odoo import fields, models

class ResPartner(models.Model):
    _inherit = 'res.partner'

    restrict_mail = fields.Boolean(string="Restrict mail")

