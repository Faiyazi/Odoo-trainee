from odoo import models,fields,api
 
class ReportProjectTimesheet(models.AbstractModel):
    _name = "report.project_task_timesheet_report.pdf_task_report"
    _description = "Project Task Timesheet Report"
 
    @api.model
    def _get_report_values(self,docids, data=None):
        date_start = data.get("date_start")
        date_end = data.get("date_end")
 
        domain = [
            ("date", '>=', date_start),
            ('date', '<=', date_end),
        ]
        company = self.env.company
        timesheets = self.env["account.analytic.line"].sudo().search(domain,order="project_id, task_id, date")
        grouped_data = {}
 
        for ts in timesheets:
            project = ts.project_id
            task = ts.task_id
 
            if project not in grouped_data:
                grouped_data[project] = {}
 
            if task not in grouped_data[project]:
                grouped_data[project][task] = []
 
            grouped_data[project][task].append(ts)
        return {
            "doc_ids" : timesheets.ids,
            "doc_model" : "account.analytic.line",
            "data" : data,
            "company" : company,
            "grouped_data" : grouped_data,
        }