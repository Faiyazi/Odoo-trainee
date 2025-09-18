from odoo import models, fields

class ResCountryState(models.Model):
    _inherit = 'res.country.state'
   

    name = fields.Char(string='State Name', required=True,translate=True)