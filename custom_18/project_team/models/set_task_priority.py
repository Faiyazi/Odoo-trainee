from odoo import models, fields

class SetTaskPriority(models.TransientModel):
    _name = 'set.task.priority'
    _description = 'Set Priority of Task'


    priority = fields.Selection([
        ('0', 'Normal'),
        ('1', 'High')
    ], string="Priority", required=True)


    def action_add_priority(self):
        print("\n\n\n\n\n\n------------------>",self)
        active_ids = self.env.context.get('active_ids', [])
        if active_ids:
            tasks = self.env['project.task'].browse(active_ids)
            tasks.write({'priority': self.priority})
        return {'type': 'ir.actions.act_window_close'}

