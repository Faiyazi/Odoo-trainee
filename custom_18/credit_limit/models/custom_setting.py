from odoo import fields, models

class ResConfigSettings(models.TransientModel):
    _inherit ='res.config.settings'

    credit_limit = fields.Float(string="Credit limit",config_parameter='credit_limit')

