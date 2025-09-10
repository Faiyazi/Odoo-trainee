from odoo import models, fields ,api
import re

from odoo.exceptions import ValidationError


class ProjectTaskChecklist(models.Model):
    _name = 'project.task.checklist'
    _description = 'Project Task Checklist'
    _inherits = {'project.task': 'task_id'}

    task_id = fields.Many2one("project.task", string="Task")



    @api.constrains('email')

    def _email_Checked(self):
        for rec in self:
            if rec.email and not re.match((r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[A-Za-z]{2,}$'),rec.email):
                raise ValidationError("email don't matches ")

    _sql_constraints = [(
        'unique_email','unique[email]','Email must be unique!'
    )]

