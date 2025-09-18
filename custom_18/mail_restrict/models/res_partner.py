from odoo import models, fields


class ResPartner(models.Model):
    _inherit = 'res.partner'

    restrict_mail = fields.Boolean(string='Restrict Mail')