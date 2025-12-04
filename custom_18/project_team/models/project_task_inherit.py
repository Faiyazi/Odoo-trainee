from odoo import models, fields, api, _ 
from odoo.exceptions import ValidationError
from datetime import datetime


class ProjectTask(models.Model):
    _inherit = 'project.task'


    date_assign_1 = fields.Datetime(string='Assign Date')
    hide_date_assign = fields.Boolean(string="Hide Assign Date", compute="_compute_hide_date_assign")

    @api.depends('stage_id')
    def _compute_hide_date_assign(self):
        for task in self:
            task.hide_date_assign = task.stage_id.name == 'Done'

    @api.model_create_multi
    def create(self,vals_list):
        now = datetime.now()
        for vals in vals_list:
            vals['date_assign_1']= now
        return super().create(vals_list)
    
    def write(self,vals):
        now = datetime.now()

        if vals.get('date_assign_1'):
            user_date= datetime.strptime(vals['date_assign_1'], "%Y-%m-%d %H:%M:%S")
            if user_date < now:
            
             raise ValidationError(_("You cannot modify Assign Date."))    
        
        return super().write(vals)
    
    def unlink(self):
        for task in self:
            if task.stage_id.name == 'In Progress':
                raise ValidationError(_("You cannot delete a task that is In Progress."))
        return super().unlink()











    