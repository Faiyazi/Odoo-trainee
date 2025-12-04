# -*- coding: utf-8 -*-
##############################################################################
#                                                                            #
# Part of Caret IT Solutions Pvt. Ltd. (Website: www.caretit.com).           #
# See LICENSE file for full copyright and licensing details.                 #
#                                                                            #
##############################################################################

from odoo import api, fields, models


class SaleOrder(models.Model):
    """Inherit sale.order Model."""
    _inherit = 'sale.order'

    source_location_id = fields.Many2one('stock.location',
                                         related='partner_id.source_location_id',
                                         string='Source Delivery Location',
                                         store=True)

    @api.constrains('partner_id')
    def partner_id_constrains_set_warehouse(self):
        """Write this method to set warehouse while change the partner."""
        for rec in self:
            if rec.source_location_id:
                warehouse_rec = self.env['stock.warehouse'].search([
                    ('lot_stock_id', '=', self.source_location_id.id)], limit=1)
                print("\n\n\n\n------------->ware",warehouse_rec)
                print("\n\n\n\n")
                rec.warehouse_id = warehouse_rec
                print("\n\n\n-------->rec",rec.warehouse_id)
