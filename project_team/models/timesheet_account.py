from  odoo import models,fields,api


class AccountTimeSheet(models.Model):
    _inherit = "account.analytic.line"

    time_sheet_id = fields.Many2one(
        'project.team.member',
        string="Team Member"
    )

    @api.model_create_multi
    def create(self, vals):
        # Wrong: self.search(vals)
        # Correct:
        if vals.get('task_id'):
            task = self.env['project.task'].search([('id', '=', vals['task_id'])], limit=1)
            # do something with task...

        return super(AccountTimeSheet, self).create(vals)



