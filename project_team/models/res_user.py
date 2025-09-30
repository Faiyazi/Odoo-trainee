from odoo import models, api


class ResUsers(models.Model):
    _inherit = 'res.users'

    @api.depends('name', 'email')
    def _compute_display_name(self):
        for user in self:
            if user.email:
                user.display_name = f"{user.name} / {user.email}"
            else:
                user.display_name = user.name or ''
