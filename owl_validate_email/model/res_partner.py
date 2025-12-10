from odoo import models, fields

class ResPartner(models.Model):
    
    _inherit = 'res.partner'

    username = fields.Char(string='Email Domain')