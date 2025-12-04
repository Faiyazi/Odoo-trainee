from odoo import models, fields, api
from odoo.exceptions import ValidationError


class ExportPdfReport(models.TransientModel):
    _name = 'export.pdf.report'
    _description = 'Export Pdf Report'


    date_start = fields.Date(string='Start Date', required=True)
    date_end = fields.Date(string='End Date', required=True)

    @api.constrains('date_start', 'date_end')
    def _check_dates(self):
        for rec in self:
            if rec.date_start and rec.date_end and rec.date_start > rec.date_end:
                raise ValidationError("Start date must be before End date.")


    def action_export_pdf(self):
        self.ensure_one()
        data = {
            "date_start": self.date_start.isoformat() if self.date_start else False,
            "date_end": self.date_end.isoformat() if self.date_end else False,
        }
       

        return self.env.ref("project_task_timesheet_report.action_report_pdf_export").report_action(docids=[], data=data)