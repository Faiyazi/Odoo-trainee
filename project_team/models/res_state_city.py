from odoo import models, fields

class StateCity(models.Model):
    _name = 'res.state.city'
    _description = 'State City'
    _order = 'name'

    name = fields.Char(string='City Name', required=True)
    state_id = fields.Many2one('res.country.state', string='State', required=True)
    country_id = fields.Many2one(
        'res.country',
        related='state_id.country_id',
        string='Country',
        store=True,
        readonly=True
    )
