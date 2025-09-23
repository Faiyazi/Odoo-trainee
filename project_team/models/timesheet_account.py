from odoo import models, fields, api


class AccountTimeSheet(models.Model):
    _inherit = "account.analytic.line"

    time_sheet_id = fields.Many2one(
        'project.team.member',
        string="Team Member",
        ondelete="set null",
        help="Team member linked to this timesheet line."
    )

  
    def create(self, vals_list):
        for vals in vals_list:

            if vals.get('task_id'):
                task = self.env['project.task'].search([('id', '=', vals['task_id'])], limit=1)
    
            elif not vals.get('name'):
                vals['name'] = "Timesheet Entry"   

        return super().create(vals)
    

    