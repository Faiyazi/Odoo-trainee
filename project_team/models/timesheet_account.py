from  odoo import models,fields,api


class AccountTimeSheet(models.Model):
    _inherit = "account.analytic.line"

    time_sheet_id = fields.Many2one(
        'project.team.member',
        string="Team Member"
    )

    @api.model

    def create(self,vals):

        task = super(AccountTimeSheet,self).search(vals)

        if task.task_id and task.employee_id:
            self.env['project.team.member'].write({
                'timesheet_ids' : task.id
            })




