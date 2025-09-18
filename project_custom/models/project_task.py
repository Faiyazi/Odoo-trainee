from odoo import models, api
from odoo.exceptions import UserError


class ProjectTask(models.Model):
    _name = "project.task"
    _inherit = ['project.task', 'start.end.mixin']
    _order = "name asc"

    # @api.model
    # def unlink(self):
    #     for task in self:
    #         if task.stage_id.name.lower != 'in progress':
    #             raise UserError('You are in progress')
    #     return super().unlink()
