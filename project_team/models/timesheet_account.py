from odoo import models, fields, api


class AccountTimeSheet(models.Model):
    _inherit = "account.analytic.line"

    time_sheet_id = fields.Many2one(
        'project.team.member',
        string="Team Member",
        ondelete="set null",   # good practice: avoid blocking deletes
        help="Team member linked to this timesheet line."
    )



    @api.model
    def create(self, vals):
        if vals.get('task_id'):
            task = self.env['project.task'].search([('id', '=', vals['task_id'])], limit=1)
            # you can do something with `task` here if needed
        return super().create(vals)
    
    @api.model
    def create(self, vals):
        # Ensure description is always set
        if not vals.get('name'):
            vals['name'] = "Timesheet Entry"   # 👈 Default fallback

        return super().create(vals)
    


    
