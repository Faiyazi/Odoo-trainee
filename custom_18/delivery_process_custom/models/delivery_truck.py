# -*- coding: utf-8 -*-
##############################################################################
#                                                                            #
# Part of Caret IT Solutions Pvt. Ltd. (Website: www.caretit.com).           #
# See LICENSE file for full copyright and licensing details.                 #
#                                                                            #
##############################################################################

from odoo import api, fields, models

class DeliveryTruckDetails(models.Model):
    _name = "delivery.truck.detail"
    _description = "Delivery Truck Details"
    _rec_name = "truck_number"

    truck_number = fields.Char(string="Truck Number")
    truck_type_id = fields.Many2one('delivery.truck.type', string="Truck Type")
    truck_loading_capacity = fields.Float(string="Loading Capacity")
    truck_uom_id = fields.Many2one('uom.uom', string='Unit of Measure', domain="[('category_id', '=', 'Weight')]")

class DeliveryTruckType(models.Model):
    _name = "delivery.truck.type"
    _description = "Delivery Truck Types"

    name = fields.Char(string="Truck Type")
    truck_count = fields.Integer(string="Number of Trucks", compute="_compute_truck_count")

    def _compute_truck_count(self):
        truck_detail_model = self.env["delivery.truck.detail"]
        groups = truck_detail_model.read_group(
            [("truck_type_id", "in", self.ids)],
            ["truck_type_id"],
            ["truck_type_id"],
            lazy=False,
        )
        data = {group["truck_type_id"][0]: group["__count"] for group in groups}
        for truck_detail in self:
            truck_detail.truck_count = data.get(truck_detail.id, 0)