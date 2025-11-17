from odoo import models, fields, api
from odoo.exceptions import ValidationError


class StartEndDate(models.AbstractModel):
    _name = 'start.end.mixin'
    _description = 'Start_End_Date'

    date_start = fields.Datetime(string="Date Start")
    date_end = fields.Datetime(string="Date End")

    @api.constrains('date_start', 'date_end')
    def _date_start_end(self):
        for rec in self:
            if rec.date_start and rec.date_end and rec.date_start > rec.date_end:
                raise ValidationError('Ending date should not be earlier than Starting Date')
