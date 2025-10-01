from odoo import models, fields, api
import logging

_logger = logging.getLogger(__name__)


class TimesheetTask(models.Model):
    _name = "timesheet.task"
    _description = "Timesheet Task"

    name = fields.Char(string='Task Name')
    description = fields.Text()
    date = fields.Datetime(string='Date')
    hours_spent = fields.Float(string='Hours Spent')

    status=fields.Char(string='status', compute='_compute_status', store=True)

    @api.model
    def create(self, vals):
        vals['name']=vals.get('name', '').upper()
        vals['name']=vals.get('description', '').title()
        record = super().create(vals)
        return record

    @api.depends('hours_spent')
    def _compute_status(self):
        for record in self:
            if record.hours_spent > 8:
                record.status = "Overworked"
            else:
                record.status = "Normal"




