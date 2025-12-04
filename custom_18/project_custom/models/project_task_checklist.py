<<<<<<< HEAD
from odoo import fields, models


class ProjectTaskChecklist(models.Model):
    """
    _inherits works:
    - The new model has a Many2one field (task_id) linking to the parent model.
    - All fields of the parent model are automatically available in the new model.
    - This is called delegation inheritance, because the new model delegates
      field storage to the parent model
    """
    _name = 'project.task.checklist'
    _description = 'Project Task Checklist'
    _inherits = {'project.task':'task_id'}

    task_id = fields.Many2one("project.task", string="Task",required=True,ondelete='cascade')

=======
from odoo import models, fields


class ProjectTaskChecklist(models.Model):
    _name = 'project.task.checklist'
    _description = 'Project Task Checklist'
    _inherits = {'project.task': 'task_id'}


    task_id = fields.Many2one('project.task', string='Task Reference', required=True, ondelete='cascade')
>>>>>>> ronak
