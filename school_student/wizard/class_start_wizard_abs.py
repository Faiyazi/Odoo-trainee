from odoo import models,fields

class AbsClassStart(models.AbstractModel):
    _name = "abs_class_start.wizard"
    _description = 'Abstract Class Start'

    start_date_t=fields.Datetime(string="Starting Time")
    end_date=fields.Datetime(string="Ending Time")
