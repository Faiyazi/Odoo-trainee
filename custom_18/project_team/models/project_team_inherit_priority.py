from odoo import models, fields

class AddPriorityWizard(models.TransientModel):
    _name = 'add.priority.wizard'
    _description = "Wizard to Set Task Priority"

    # Match the core project.task priority field
    priority = fields.Selection([
        ('0', 'Low'),
        ('1', 'High'),
       ], string="Priority", required=True)

    def add_priority(self):
        tasks = self.env['project.task'].browse(self._context.get('active_ids'))
        tasks.write({'priority': self.priority})
