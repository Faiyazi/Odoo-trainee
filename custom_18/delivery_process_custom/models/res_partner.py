# -*- coding: utf-8 -*-
##############################################################################
#                                                                            #
# Part of Caret IT Solutions Pvt. Ltd. (Website: www.caretit.com).           #
# See LICENSE file for full copyright and licensing details.                 #
#                                                                            #
##############################################################################

from odoo import fields, models


class Partner(models.Model):
    """Inherit res.partner Model."""
    _inherit = 'res.partner'

    location_id = fields.Many2one('delivery.location', string='Delivery Location')
    source_location_id = fields.Many2one('stock.location',
                                         string='Source Delivery Location')
