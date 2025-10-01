from odoo import models,fields

class SaleOrderModel(models.Model):
    _inherit = ["sale.order"]