from odoo import models, fields

class ResPartner(models.Model):
    _inherit = 'res.partner'

    is_partner_verified = fields.Boolean(
        string="Partner Verified",
    )
