from odoo import models, fields
from odoo.exceptions import UserError


class ProjectProject(models.Model):
    _inherit = 'project.project'

    contact_email = fields.Char(string='Contact Email')

    def action_send_email(self):
        print("\n\n\n========>Button Clicked<=========")
        if not self.contact_email:
            raise UserError("No email set for this project.")

        template = self.env.ref('project_functional.project_email_template')
        if template:
            template.send_mail(self.id, force_send=True)