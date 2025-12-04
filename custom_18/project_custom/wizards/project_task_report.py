from odoo import models, fields
from odoo.exceptions import UserError


class ProjectTaskReport(models.TransientModel):
    _name = 'project.task.report'
    _description = 'Project Task Report'
    _total_max_count=2

    start_date = fields.Datetime(string="Start Date", required=True)
    end_date = fields.Datetime(string="Task End Date", required=True)

    def action_project_task_report_pdf(self):
        tasks = self.env['project.task'].search([
            ('date_assign', '<=', self.end_date),
            ('date_deadline', '>=', self.start_date)
        ])
        if not tasks:
            raise UserError("No tasks found in this date range.")
        return self.env.ref('project_custom.action_report_overlapping_tasks').report_action(tasks)

    def action_project_task_report_excel(self):
        tasks = self.env['project.task'].search([
            ('date_assign', '<=', self.end_date),
            ('date_deadline', '>=', self.start_date)
        ])
        if not tasks:
            raise UserError("No tasks found in this date range.")
        return self.env.ref('project_custom.action_report_overlapping_tasks_excel').report_action(tasks)
