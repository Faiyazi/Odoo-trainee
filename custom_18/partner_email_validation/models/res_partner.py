from odoo import models, api, fields
from validate_email_address import validate_email
from odoo.exceptions import ValidationError


class ResPartner(models.Model):
    _inherit = 'res.partner'

    restrict_mail = fields.Boolean(string='Restrict Email')

    validate_email('user@example.com')

    _sql_constraints = [
        (
            'unique_email',
            'unique(email)',
            'Email address must be unique!'
        ),
    ]

    @api.constrains('email')
    def _check_email_formate(self):
        for partner in self:
            if partner.email and not validate_email(partner.email):
                raise ValidationError("Invalid email formate.")
            


    