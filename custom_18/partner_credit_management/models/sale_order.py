from odoo import api, fields, models


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    total_credit_limit = fields.Monetary(
        'Total Credit Limit',
        compute='_compute_total_credit_limit',
    )
    open_account_value = fields.Monetary(
        'Open S/O Value',
        compute='_compute_open_account_value',
    )
    total_over_due = fields.Monetary(
        'Total Over Due',
        compute='_compute_total_over_due',
    )
    current_credit_limit = fields.Monetary(
        'Current Credit Limit',
        compute='_compute_current_credit_limit',
    )

    @api.depends('partner_id')
    def _compute_total_credit_limit(self):
        '''Method to compute Total Credit Limit'''
        for rec in self:
            rec.total_credit_limit = 0.0
            if rec.partner_id:
                rec.total_credit_limit = rec.partner_id.total_credit_limit

    @api.depends('partner_id')
    def _compute_open_account_value(self):
        '''Method to compute Open S/O Value'''
        for rec in self:
            rec.open_account_value = 0.0
            if rec.partner_id:
                rec.open_account_value = rec.partner_id.open_account_value

    @api.depends('partner_id')
    def _compute_total_over_due(self):
        '''Method to compute Total Over Due'''
        for rec in self:
            rec.total_over_due = 0.0
            if rec.partner_id:
                rec.total_over_due = rec.partner_id.total_over_due

    @api.depends('partner_id')
    def _compute_current_credit_limit(self):
        '''Method to compute Current Credit Limit'''
        for rec in self:
            rec.current_credit_limit = 0.0
            if rec.partner_id:
                rec.current_credit_limit = rec.partner_id.current_credit_limit
