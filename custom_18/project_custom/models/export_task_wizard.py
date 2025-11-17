from odoo import models, fields


class ExportTaskWizard(models.TransientModel):
    _name = 'export.task.wizard'
    _description = 'Export Overlapping Task'

    date_start = fields.Date(string="Start Date", required=True)
    date_end = fields.Date(string="End Date", required=True)

    
    def action_export_task(self):
        print("\n\n\n-----------> Export button clicked")

        return self.env.ref("project_custom.action_report_pdf_export").report_action(self)
    
    def action_export_task_excel(self):
        print("\n\n\n-----------> Export button clicked........")

        tasks = self.env['project.task'].search([
            ('date_assign', '>=', self.date_start),
            ('date_deadline', '<=', self.date_end)
        ])

        print("tasks\n-----------> ttttttttttt",tasks)
        for task in tasks:
            print("Task: {task.name} | Start: {task.date_assign} | End: {task.date_deadline}")
        print("\n----------------->ppppppp")

        return self.env.ref("project_custom.action_report_excel_export").report_action(self)
        

    
