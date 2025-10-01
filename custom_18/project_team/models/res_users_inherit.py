from odoo import models, fields, api

class ResUsers(models.Model):
    _inherit = 'res.users'

    @api.depends()
    def _compute_display_name(self):
        for user in self:
            user.display_name = f"{user.name} / {user.email}"