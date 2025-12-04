from odoo import models, fields

class ResStateCity(models.Model):
    _name = 'res.state.city'
    _description = 'City'

    name = fields.Char(string='City Name', required=True,translate=True)
    state_id= fields.Many2one('res.country.state', string='State', required=True)
    country_id = fields.Many2one(related='state_id.country_id', string='Country')