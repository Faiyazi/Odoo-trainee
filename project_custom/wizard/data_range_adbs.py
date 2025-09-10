from odoo import models

class DataTimeSheet(models.AbstractModel):
    _name = 'TimeSheetata'
    
    def data_time_sheet(self, date_start, date_end):
        for rec in self.env['account.analytic.line'].search([('date', '>=', date_start), ('date', '<=', date_end)]):
            tasks = rec.mapped('task_id')
        return tasks