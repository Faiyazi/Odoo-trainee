# -*- coding: utf-8 -*-
##############################################################################
#                                                                            #
# Part of Caret IT Solutions Pvt. Ltd. (Website: www.caretit.com).           #
# See LICENSE file for full copyright and licensing details.                 #
#                                                                            #
##############################################################################

from odoo import api, fields, models


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    login_company = fields.Char(
        'res.company',
        default=lambda self: self.env.company.name,
        compute='_compute_login_company',
    )

    @api.depends_context('company')
    def _compute_login_company(self):
        '''Method to compute Login Company Name'''
        for rec in self:
            rec.login_company = self.env.company.name


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    login_company = fields.Char(
        'res.company',
        default=lambda self: self.env.company.name,
        compute='_compute_login_company',
    )

    @api.depends_context('company')
    def _compute_login_company(self):
        '''Method to compute Login Company Name'''
        for rec in self:
            rec.login_company = self.env.company.name

