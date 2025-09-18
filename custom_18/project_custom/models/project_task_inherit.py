from odoo import models

class ProjectTask(models.Model):
    _name = 'project.task'
    _inherit = ['project.task', 'startend.mixin']
    _order = 'name'
