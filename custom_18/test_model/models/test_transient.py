from odoo import models, fields, api

class TestTransientModel(models.TransientModel):
    _name = 'test.model.transient'
    _description = 'test transient model'
