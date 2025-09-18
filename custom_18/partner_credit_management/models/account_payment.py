from odoo import models, fields

class AccountPayment(models.Model):
    _inherit = 'account.payment'


    # Override this two fields from standard just to pass store=true attribute and use this in our custom calculation
    reconciled_invoices_count = fields.Integer(string="# Reconciled Invoices",
        compute="_compute_stat_buttons_from_reconciliation", store=True)
    reconciled_bills_count = fields.Integer(string="# Reconciled Bills",
        compute="_compute_stat_buttons_from_reconciliation", store=True)