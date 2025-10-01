from odoo import models, _
from odoo.exceptions import UserError

class ProjectTask(models.Model):
    _inherit = 'project.task'
    _order = 'name asc'


    def unlink(self):
        for task in self:
            if task.stage_id.name == 'In Progress':
                raise UserError(_("You cannot delete a task that is In Progress."))
        return super().unlink()
 