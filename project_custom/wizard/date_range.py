from odoo import models

class DataRangeSelection(models.TransientModel):
    _name = 'datarange.wizard'
    _description = 'Data Range Selection'
    _inherit = 'start.end.mixin'

    def _get_task(self):
        return self.env['project.task'].search([
            ('date_start', '>=', self.date_start),
            ('date_end', '<=', self.date_end),
        ])

    def action_print_report_pdf(self):
        tasks = self._get_task()
        return self.env.ref('project_custom.project_task_report').report_action(tasks)

    def action_print_report_xlsx(self):
        tasks = self._get_task()
        return self.env.ref('project_custom.project_task_report_xlsx').report_action(tasks)
