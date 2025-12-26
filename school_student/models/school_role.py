from odoo import models, fields, api

class SchoolRole(models.Model):
    _name = 'school.role'
    _description = 'School Role'
    _rec_name = 'role'
    
    
    role = fields.Char('Create role')
    
