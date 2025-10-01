from odoo import models


class SaleOrder(models.Model):
    _inherit = 'sale.order'


    # def write(self, vals):
    #     res = super().write(vals)

    #     for quant in self:
    #         if quant.quantity < 50:
    #             quant.quantity = 50

    #     return res
