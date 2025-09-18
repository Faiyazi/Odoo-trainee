import re
from odoo import models, fields, api
from odoo.exceptions import ValidationError


class ResPartner(models.Model):
    _inherit = 'res.partner'
    _sql_constraints = [
    ('unique_email', 'unique(email)', 'Email must be unique!')
        ]

    restrict_mail = fields.Boolean(
        string="Restrict Emails",
        help="If enabled, this partner will not receive chatter emails."
    )


    @api.constrains('email')
    def _check_email(self):
        email_pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        for record in self:
            if record.email and not re.match(email_pattern, record.email):
                raise ValidationError(f"Invalid Email: {record.email}")
            



    


