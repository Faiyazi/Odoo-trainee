# -*- coding: utf-8 -*-
##############################################################################
#                                                                            #
# Part of Caret IT Solutions Pvt. Ltd. (Website: www.caretit.com).           #
# See LICENSE file for full copyright and licensing details.                 #
#                                                                            #
##############################################################################

from odoo import api, fields, models
from lxml import etree
import json

class Picking(models.Model):
    _inherit = "stock.picking"

    delivery_location_id = fields.Many2one(comodel_name="delivery.location", related='partner_id.location_id', string='Delivery Location', copy=False, store=True)
    delivery_truck_id = fields.Many2one('delivery.truck.detail', string="Select Truck")
    truck_type_id = fields.Many2one('delivery.truck.type', string="Truck Type")
    truck_loading_capacity = fields.Float(string="Loading Capacity")
    truck_uom_id = fields.Many2one('uom.uom', string='Unit of Measure', domain="[('category_id', '=', 'Weight')]")

    @api.onchange('delivery_truck_id')
    def onchange_delivery_truck_id(self):
        TruckObj = self.env['delivery.truck.detail'].search([('id', '=', self.delivery_truck_id.id)])
        print("\n\n---------->111111111",TruckObj)
        if TruckObj:
            self.truck_type_id = TruckObj.truck_type_id
            print("\n\n\n----------->22222222",self.truck_type_id)
            self.truck_loading_capacity = TruckObj.truck_loading_capacity
            print("\n\n\n----------->3333333",self.truck_loading_capacity)
            self.truck_uom_id = TruckObj.truck_uom_id
            print("\n\n\n----------->444444444",self.truck_uom_id)
        else:
            self.truck_type_id = False
            print("\n\n\n----------->555555555",self.truck_type_id)
            self.truck_loading_capacity = 0.00
            print("\n\n\n----------->666666666",self.truck_loading_capacity)
            self.truck_uom_id = False
            print("\n\n\n----------->777777777",self.truck_uom_id)

    def fields_view_get(self, view_id=None, view_type='tree', toolbar=False, submenu=False):
        result = super(Picking, self).fields_view_get(view_id=view_id, view_type=view_type, toolbar=toolbar, submenu=submenu)
        if not self.env.context.get('show_the_column', False) and view_type == 'tree':
            doc = etree.fromstring(result['arch'])
            if self.env.company.name != 'FUGEN UK LTD':
                fields_1 = doc.xpath("//field[@name='delivery_location_id']")
                for field in fields_1:
                    field.set('invisible', '1')
                    modifiers = json.loads(field.get('modifiers', '{}'))
                    modifiers['tree_invisible'] = True
                    modifiers['column_invisible'] = True
                    field.set('modifiers', json.dumps(modifiers))
                result['arch'] = etree.tostring(doc)

                fields_2 = doc.xpath("//field[@name='delivery_truck_id']")
                for field in fields_2:
                    field.set('invisible', '1')
                    modifiers = json.loads(field.get('modifiers', '{}'))
                    modifiers['tree_invisible'] = True
                    modifiers['column_invisible'] = True
                    field.set('modifiers', json.dumps(modifiers))
                result['arch'] = etree.tostring(doc)

                fields_3 = doc.xpath("//field[@name='truck_type_id']")
                for field in fields_3:
                    field.set('invisible', '1')
                    modifiers = json.loads(field.get('modifiers', '{}'))
                    modifiers['tree_invisible'] = True
                    modifiers['column_invisible'] = True
                    field.set('modifiers', json.dumps(modifiers))
                result['arch'] = etree.tostring(doc)

                fields_4 = doc.xpath("//field[@name='truck_loading_capacity']")
                for field in fields_4:
                    field.set('invisible', '1')
                    modifiers = json.loads(field.get('modifiers', '{}'))
                    modifiers['tree_invisible'] = True
                    modifiers['column_invisible'] = True
                    field.set('modifiers', json.dumps(modifiers))
                result['arch'] = etree.tostring(doc)

                fields_5 = doc.xpath("//field[@name='truck_uom_id']")
                for field in fields_5:
                    field.set('invisible', '1')
                    modifiers = json.loads(field.get('modifiers', '{}'))
                    modifiers['tree_invisible'] = True
                    modifiers['column_invisible'] = True
                    field.set('modifiers', json.dumps(modifiers))
                result['arch'] = etree.tostring(doc)

        if view_type == 'search':
            doc = etree.fromstring(result['arch'])
            if self.env.company.name != 'FUGEN UK LTD':
                filter_1 = doc.xpath("//filter[@name='group_by_delivery_location']")
                for filter in filter_1:
                    filter.set('invisible', '1')
                    modifiers = json.loads(filter.get('modifiers', '{}'))
                    modifiers['invisible'] = True
                    filter.set('modifiers', json.dumps(modifiers))
                result['arch'] = etree.tostring(doc)

                filter_2 = doc.xpath("//filter[@name='group_by_delivery_truck']")
                for filter in filter_2:
                    filter.set('invisible', '1')
                    modifiers = json.loads(filter.get('modifiers', '{}'))
                    modifiers['invisible'] = True
                    filter.set('modifiers', json.dumps(modifiers))
                result['arch'] = etree.tostring(doc)

        return result