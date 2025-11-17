from odoo import models,fields


class CustomTask(models.TransientModel):
    _inherit = 'res.config.settings'

    credit = fields.Float(string='Credit Limits',config_parameter="custom_task.credit")

