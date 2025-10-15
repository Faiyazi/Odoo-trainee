from odoo import models, fields, api
from odoo.exceptions import ValidationError


class ProjectTask(models.Model):
    _inherit = ['project.task']


    assign_date = fields.Datetime(string='Assign date')
    
    @api.model_create_multi
    def create(self, vals_list):
        # Support single dict and list of dicts
        if isinstance(vals_list, dict):
            vals_list = [vals_list]

        for vals in vals_list:
            # Set assign_date if not provided
            if 'assign_date' not in vals:
                vals['assign_date'] = fields.Datetime.now()

            # Validate assign_date
            if vals['assign_date'] < fields.Datetime.now():
                raise ValidationError("Past date not allowed")

        # Call super with the whole list
        return super(ProjectTask, self).create(vals_list)

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



