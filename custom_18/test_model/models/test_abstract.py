from odoo import api, fields, models

class TestAbstractModel(models.AbstractModel):
    _name = 'test.model.abstract'
    _description = 'test abstract model'

    name=fields.Char(string='test name',required=True)
    dob=fields.Date(string='date of birth',required=True)
    address=fields.Char(string='address',required=True)

