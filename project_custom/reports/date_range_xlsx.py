from odoo import models

class DateRangeXlsx(models.AbstractModel):
    _name = 'report.project_task.project_task_xlsx'
    _description = 'Project Task XLSX Report'
    _inherit = 'report.report_xlsx.abstract'

    def generate_xlsx_report(self, workbook, data, objects):
        # Add a worksheet
        sheet = workbook.add_worksheet("Tasks")

        # Define some formats
        bold = workbook.add_format({'bold': True})

        # Example: Writing headers
        sheet.write(0, 0, "Task Name", bold)
        sheet.write(0, 1, "Assigned To", bold)
        sheet.write(0, 2, "Deadline", bold)

        row = 1
        for task in objects:
            sheet.write(row, 0, ', '.join(task.user_ids.mapped('name')) or '')  # Users
            sheet.write(row, 1, str(task.date_start or ''))  # Start date
            sheet.write(row, 2, str(task.date_deadline or ''))  # Deadline
            row += 1
