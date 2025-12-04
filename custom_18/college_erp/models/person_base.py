from odoo import models,fields

class PersonBase(models.Model):
    _name = "person.base"
    _description = "Base class for Person"


    name = fields.Char(string="Full Name", required=True)
    email = fields.Char(string="Email")
    phone = fields.Char(string="Phone Number")

