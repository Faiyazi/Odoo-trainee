from odoo import models

class SaleOrder(models.Model):
    _inherit = 'sale.order'


    def action_wizard_open(self):
        print("\n\n\n--------->Button Was Clicked<----------")
        return{
            'name':'Excel',
            'type':'ir.actions.act_window',
            'view_mode':'form',
            'res_model':'sale.order.wizard',
            'target':'new',
            'context':{'default_sale_id':self.id},
        }