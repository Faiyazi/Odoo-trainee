from odoo import fields,models,api

class TestingInherit(models.Model):
    _inherit = "res.partner"
    
    
    new_xyz = fields.Char("NEW XYZ")