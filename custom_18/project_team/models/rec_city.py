from odoo import models,fields

class RecCity(models.Model):
    _name="res.state.city"
    _description="City"
    _rec_name='name'

    name=fields.Char(string="City Name",required=True)
    state_id= fields.Many2one('res.country.state', string="State", required=True,ondelete="cascade")
    country_id = fields.Many2one('res.country',related="state_id.country_id", string="Country", store=True,
                                 readonly=True)
