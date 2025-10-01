from odoo import fields, models, api
from odoo.exceptions import ValidationError
import re

class Partner(models.Model):
    _inherit = 'res.partner'

    _sql_constraints = [
        ('email_unique_partner', 'UNIQUE(email)', 'Email is already registered.')
    ]

    @api.constrains('email')
    def _check_email(self):
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        for partner in self:
            if partner.email and not re.match(pattern, partner.email):
                raise ValidationError("Invalid email format.")
