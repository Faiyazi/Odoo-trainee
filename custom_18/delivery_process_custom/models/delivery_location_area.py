# -*- coding: utf-8 -*-
##############################################################################
#                                                                            #
# Part of Caret IT Solutions Pvt. Ltd. (Website: www.caretit.com).           #
# See LICENSE file for full copyright and licensing details.                 #
#                                                                            #
##############################################################################

from odoo import api, fields, models

class DeliveryLocationName(models.Model):
    _name = "delivery.location"
    _description = "Delivery Location"

    name = fields.Text(string="Location Name", required=True)
    # area_count = fields.Integer(string="Number of Areas", compute="_compute_area_count")
    contact_count = fields.Integer(string="Number of Contacts", compute="_compute_contact_count")

    # def _compute_area_count(self):
    #     area_model = self.env["delivery.area"]
    #     groups = area_model.read_group(
    #         [("location_id", "in", self.ids)],
    #         ["location_id"],
    #         ["location_id"],
    #         lazy=False,
    #     )
    #     data = {group["location_id"][0]: group["__count"] for group in groups}
    #     for area in self:
    #         area.area_count = data.get(area.id, 0)

    def _compute_contact_count(self):
        '''Compute COunt of Related Contacts in the Delivery Location Form View'''
        contact_detail_model = self.env["res.partner"]
        groups = contact_detail_model.read_group(
            [("location_id", "in", self.ids)],
            ["location_id"],
            ["location_id"],
            lazy=False,
        )
        data = {group["location_id"][0]: group["__count"] for group in groups}
        for contact_detail in self:
            contact_detail.contact_count = data.get(contact_detail.id, 0)


# class DeliveryAreaName(models.Model):
#     _name = "delivery.area"
#     _description = "Delivery Area"
#
#     name = fields.Text(string="Area Name", required=True)
#     area_zip = fields.Char(string="ZIP")
#     location_id = fields.Many2one('delivery.location', string="Location")
