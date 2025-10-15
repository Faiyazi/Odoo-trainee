from odoo import models, api

class TaskTimesheetReport(models.AbstractModel):
    _name = 'report.project_task_timesheet_report.report_task_timesheet'
    _description = 'Task Timesheet PDF Report'

    @api.model
    def _get_report_values(self, docids, data=None):
        date_start = data.get('date_start')
        date_end = data.get('date_end')

        timesheets = self.env['account.analytic.line'].search([
            ('date', '>=', date_start),
            ('date', '<=', date_end),
            ('task_id', '!=', False)
        ], order='project_id, task_id, date')
        print("______Timesheet Report_____________", timesheets)

        projects_dict = {}

        for ts in timesheets:
            project = ts.project_id
            task = ts.task_id

            # Initialize project and task in one go
            project_data = projects_dict.setdefault(project.id, {
                'project': project,
                'tasks': {},
                'total_hours': 0.0
            })
            print("___________Project_data________________", project_data)

            task_data = project_data['tasks'].setdefault(task.id, {
                'task': task,
                'timesheets': [],
                'total_hours': 0.0
            })
            print("_________________Task_data___________________", task_data)

            task_data['timesheets'].append(ts)
            task_data['total_hours'] += ts.unit_amount or 0.0
            project_data['total_hours'] += ts.unit_amount or 0.0

        # Convert tasks dict to list for QWeb
        for p in projects_dict.values():
            p['tasks'] = list(p['tasks'].values())
        print("___________Project_dict____________________", projects_dict)

        return {
            'projects': list(projects_dict.values()),
            'date_start': date_start,
            'date_end': date_end,
            'company': self.env.company,
        }
