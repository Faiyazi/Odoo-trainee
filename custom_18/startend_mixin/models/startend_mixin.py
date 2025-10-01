from odoo import fields,models,api
from odoo.exceptions import ValidationError

class StartendMixin(models.AbstractModel):
    _name = 'startend_mixin'
    _description = 'Startend Mixin'

    start_date = fields.Date(string="Start date")
    end_date = fields.Date(string="End date")

    @api.constrains('start_date', 'end_date')
    def _check_start_date(self):
        for rec in self:
            if rec.start_date and rec.end_date and rec.start_date > rec.end_date:
                raise ValidationError("Start date cannot be greater than End date")