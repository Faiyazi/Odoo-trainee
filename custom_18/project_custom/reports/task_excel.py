from odoo import models

class TaskXls(models.AbstractModel):
    _name = 'report.project_custom.task_report_excel'
    _inherit = 'report.report_xlsx.abstract'

    def generate_xlsx_report(self, workbook, data, wizard):
        print("\n\n\n\n\n\n\n\n\n\n\n\n-------------------------->",wizard)
        sheet = workbook.add_worksheet('Task Report')

       
        headers = ['Name', 'Assigned To', 'Start Date', 'End Date', 'Deadline', 'Stage']
        for col, header in enumerate(headers):
            sheet.write(0, col, header)

        
        domain = [
            ('date_assign', '>=', wizard.date_start),
            ('date_deadline', '<=', wizard.date_end)
        ]
        tasks = self.env['project.task'].search(domain)

        
        for row, task in enumerate(tasks, start=1):
            sheet.write(row, 0, task.name or '')
            sheet.write(row, 1, ','.join(task.user_ids.mapped('name')) or '')
            sheet.write(row, 2, str(task.date_assign or ''))
            sheet.write(row, 3, str(task.date_deadline or ''))
            sheet.write(row, 4, str(task.date_deadline or ''))
            sheet.write(row, 5, task.stage_id.name or '')
