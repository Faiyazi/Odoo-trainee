from odoo import models, fields

class ProjectTaskReport(models.TransientModel):
    _name = 'project.task.report'
    _description = 'Project Task Report'

    date_start = fields.Date(string="Start Date", required=True)
    date_end = fields.Date(string="End Date", required=True)

    def action_project_task_report_pdf(self):
        data = {
            'date_start': self.date_start,
            'date_end': self.date_end,
        }
        return self.env.ref('project_task_timesheet_report.action_report_task_timesheet').report_action(self, data=data)
