from odoo import models, fields

class ResPartner(models.Model):
    
    _inherit = 'res.partner'

    new_name = fields.Char(string='New Name')