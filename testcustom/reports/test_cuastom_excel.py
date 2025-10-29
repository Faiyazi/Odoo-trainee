from odoo import models

class TestCustomExcel(models.AbstractModel):
    _name = 'report.testcustom.report_testcustom_xlsx'
    _inherit = 'report.report_xlsx.abstract'
    _description = 'Report Test Custom'

    def generate_xlsx_report(self, workbook, data, partners):
        # for obj in partners:
        #     report_name = obj.name
        sheet=workbook.add_worksheet('Faiyaz')
        bold = workbook.add_format({'bold': True})
        sheet.write(2, 2, 'Name', bold)
        sheet.write(2, 3, partners.name, bold)
        