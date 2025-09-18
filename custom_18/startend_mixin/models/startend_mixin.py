from odoo import models, fields, api
from odoo.exceptions import ValidationError 


class StartendMixin(models.AbstractModel):
    _name = 'startend.mixin'
    _description = 'Start and end date mixin'


    date_start = fields.Date(string='Start Date')
    date_end = fields.Date(string='End Date')

    @api.constrains('date_start', 'date_end')
    def _check_date_range(self):
        for record in self:
            if record.date_start and record.date_end:
                if record.date_start > record.date_end:
                    raise ValidationError("Start date cannot be after end date.")
            
                
