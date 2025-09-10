from odoo import models,fields


class ClassStartWizard(models.TransientModel):
    _name = 'class_start.wizard'
    _description = 'Class Start'

    start_date=fields.Datetime(string="Starting Date")

