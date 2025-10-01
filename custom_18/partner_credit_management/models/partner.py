from odoo import api, fields, models


class Partner(models.Model):
    _inherit = 'res.partner'

    total_credit_limit = fields.Monetary(
        'Total Credit Limit',
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
   
    total_due_custom = fields.Monetary(string="Open Balance",
                                       )

    @api.depends('invoice_ids', 'invoice_ids.amount_residual')
    def _compute_open_account_value(self):
        '''Method to compute Open S/O Value'''
        for rec in self:
            invoices = rec.invoice_ids.filtered(lambda invoice: invoice.company_id.id == self.env.company.id)
            open_account_value = sum([
                rec.amount_residual for rec in invoices if rec.state in ['draft', 'posted'] and rec.payment_state in ['partial', 'not_paid'] and rec.move_type!='out_refund'])
            rec.open_account_value = open_account_value

    @api.depends('invoice_ids', 'invoice_ids.amount_residual')
    def _compute_total_over_due(self):
        '''Method to compute Total Over Due'''
        for rec in self:
            overdue_invoices = self.env['account.move']
            invoices = rec.invoice_ids.filtered(lambda invoice: invoice.company_id.id == self.env.company.id)
            for inv in invoices:
                if inv.state != 'cancel' and inv.invoice_date_due and inv.invoice_date_due < fields.Date.today() and inv.payment_state != 'paid':
                    overdue_invoices |= inv
            total_over_due = sum([rec.amount_residual for rec in overdue_invoices])
            rec.total_over_due = total_over_due

    # Do not remove this commented code.
    # Because in new requirement this compute method calculation are changesd,
    # but may be client ask about it for same again in future.
    # @api.depends('total_credit_limit', 'open_account_value')
    # def _compute_current_credit_limit(self):
    #     '''Method to compute Current Credit Limit'''
    #     for rec in self:
    #         entry_total_debit = 0.0
    #         entry_total_credit =  0.0
    #         invoices = rec.invoice_ids.filtered(lambda invoice: invoice.company_id.id == self.env.company.id)
    #         # add ledger entry amount, credit plus, debit minus
    #         entries = self.env['account.move.line'].sudo().search([('partner_id', '=', rec.id),('move_id.move_type', '=', 'entry')])
    #         for line in entries:
    #             entry_total_debit += line.debit
    #             entry_total_credit += line.credit
    #         # add directly(without Invoice or Bills) created payments amount calculation, cutomer payment plus, vendor payment minus from current credit limit
    #         payments_without_invoice = self.env['account.payment'].sudo().search([('partner_id', '=', rec.id),('state', 'in', ['draft', 'posted']),('reconciled_invoices_count', '=', 0)])
    #         payments_without_bills = self.env['account.payment'].sudo().search([('partner_id', '=', rec.id),('state', 'in', ['draft', 'posted']),('reconciled_bills_count', '=', 0)])
    #         customer_payment_amount = sum(record.amount for record in payments_without_invoice if record.partner_type == 'customer')
    #         vendor_payment_amount = sum(record.amount for record in payments_without_bills if record.partner_type == 'supplier')
    #         # to deduct invoice amount
    #         invoice_amount = sum([
    #             invoice.amount_residual for invoice in invoices if invoice.state in ['draft', 'posted'] and invoice.payment_state in ['partial', 'not_paid'] and invoice.move_type!='out_refund'])
    #         # to append credit amount
    #         credit_amount = sum([
    #              rec.amount_total for rec in invoices if rec.state in ['draft', 'posted'] and rec.payment_state in ['partial', 'not_paid'] and rec.move_type=='out_refund'])
    #         rec.current_credit_limit = rec.total_credit_limit - invoice_amount + credit_amount + entry_total_credit - entry_total_debit + customer_payment_amount - vendor_payment_amount


    @api.depends('total_credit_limit')
    def _compute_current_credit_limit(self):
        '''method to compute current credit limit'''
        for rec in self:
            rec.current_credit_limit = rec.total_credit_limit - rec.total_due_custom
