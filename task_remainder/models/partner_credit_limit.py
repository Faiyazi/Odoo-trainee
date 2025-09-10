from odoo import models,fields

class PartnerCredits(models.Model):
    _inherit = 'res.partner'

    partner_credits_limits=fields.Float(string='Credits Limits',config_parameter="custom_task.credit")