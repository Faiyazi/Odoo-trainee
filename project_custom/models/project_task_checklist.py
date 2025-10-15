from odoo import models, fields ,api
import re

from odoo.exceptions import ValidationError


class ProjectTaskChecklist(models.Model):
    _name = 'project.task.checklist'
    _description = 'Project Task Checklist'
    _inherits = {'project.task': 'task_id'}
    


    task_id = fields.Many2one('project.task', required=True, ondelete='cascade')


