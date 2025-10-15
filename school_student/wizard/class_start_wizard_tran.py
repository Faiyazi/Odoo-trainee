from odoo import models,fields

class TranClassStartWizard(models.TransientModel):
    _name = 'tran_class_start.wizard'
    _inherit = 'abs_class_start.wizard'
    _description = 'Transient Class Start'

    name=fields.Many2one('school.student',string="Student Name")

