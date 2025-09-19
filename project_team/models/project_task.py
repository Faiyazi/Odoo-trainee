from odoo import models, fields, api
from odoo.exceptions import ValidationError


class ProjectTask(models.Model):
    _inherit = ['project.task']


    assign_date = fields.Datetime(string='Assign date')

    @api.model
    def create(self, vals):
        vals['assign_date'] = fields.Datetime.now()

        if "assign_date" in vals:
            if vals['assign_date'] < fields.Datetime.now():
                raise ValidationError('past date not allow')

        return super(ProjectTask, self).create(vals)

    def write(self, vals):
        if "assign_date" in vals:
            if vals['assign_date'] < fields.Datetime.now():
                raise ValidationError('past date not allow')

        return super(ProjectTask, self).write(vals)

    # def unlink(self):
    #     for task in self:
    #         if  task.stage_id.name != 'Done' :
    #             raise ValidationError('Task is not done yet')

    #     return super(ProjectTask, self).unlink()



