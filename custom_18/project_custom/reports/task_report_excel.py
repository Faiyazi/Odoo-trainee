from odoo import models

class TaskProjectReport(models.AbstractModel):
    _name = 'report.project_custom.report_task_overlapping_excel'
    _description = 'Project Task XLSX Report'
    _inherit = 'report.report_xlsx.abstract'

    def generate_xlsx_report(self, workbook, data, objects):#data is the parameter of this function
        sheet = workbook.add_worksheet("Tasks")

        bold = workbook.add_format({'bold': True})
        #write the header
        sheet.write(0, 0, "Task Name", bold)
        sheet.write(0, 1, "Project", bold)
        sheet.write(0, 2, "Assigned To", bold)
        sheet.write(0, 3, "Start Date", bold)
        sheet.write(0, 4, "Deadline", bold)

        #Write the data
        row = 1
        for task in objects:
            sheet.write(row, 0, task.name)
            sheet.write(row, 1, task.project_id.name)
            sheet.write(row, 2, ', '.join(task.user_ids.mapped('name')))
            sheet.write(row, 3, str(task.date_assign))
            sheet.write(row, 4, str(task.date_deadline))
            row += 1