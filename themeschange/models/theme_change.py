from odoo import models,fields

class ThemeChange(models.Model):
    _name ="theme.change"
    _description="Theme Change"
    
    
    name = fields.Char(string="Name")
    menubar = fields.Char(string="menu bar")
    menuslide = fields.Char(string="Mneu Slide")
    theme = fields.Char(string="Theme")