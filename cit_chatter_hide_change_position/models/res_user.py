from odoo import models, fields

class ResUsers(models.Model):
    _inherit = "res.users"

    hide_chatter = fields.Boolean(string="Hide Chatter",default=False)
