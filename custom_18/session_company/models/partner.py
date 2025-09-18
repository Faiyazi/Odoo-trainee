# -*- coding: utf-8 -*-
##############################################################################
#                                                                            #
# Part of Caret IT Solutions Pvt. Ltd. (Website: www.caretit.com).           #
# See LICENSE file for full copyright and licensing details.                 #
#                                                                            #
##############################################################################

from odoo import api, fields, models


class Partner(models.Model):
    _inherit = 'res.partner'

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

