<<<<<<< HEAD
from odoo import fields,models,api

class ProjectTask(models.Model):
    _name = 'project.task'
    _inherit = ['project.task','startend_mixin']
=======
from odoo import models

class ProjectTask(models.Model):
    _name = 'project.task'
    _inherit = ['project.task', 'startend.mixin']
    _order = 'name'
>>>>>>> ronak
