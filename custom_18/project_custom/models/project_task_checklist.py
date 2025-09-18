from odoo import models, fields


class ProjectTaskChecklist(models.Model):
    _name = 'project.task.checklist'
    _description = 'Project Task Checklist'
    _inherits = {'project.task': 'task_id'}


    task_id = fields.Many2one('project.task', string='Task Reference', required=True, ondelete='cascade')