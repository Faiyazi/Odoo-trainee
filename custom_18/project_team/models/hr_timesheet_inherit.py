from odoo import models, fields, api

class AccountAnalyticLine(models.Model):
    _inherit = "account.analytic.line"

    project_team_member_id = fields.Many2one(
        'project.team.member',
        string='Project Team Member',
    )

    @api.model
    def create(self, vals):
        # Create original timesheet
        if vals.get('employee_id'):
            member = self.env['project.team.member'].search(
                [('employee_id', '=', vals['employee_id'])], limit=1
            )
            if member and vals.get('task_id'):
                member.write({'task_ids': [(4, vals['task_id'])]})
        record = super(AccountAnalyticLine, self).create(vals)

        return record
