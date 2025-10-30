from odoo import models, fields, api

class ResPartnerInherit(models.Model):
    _inherit = 'res.partner'

    credit_limit = fields.Float(string="Credit Limit")

    credit_limit_status = fields.Float(
        string="Credit Limit Status",
     )

    # @api.depends('credit_limit')
    # def _compute_credit_limit_status(self):
    #     for rec in self:
    #         rec.credit_limit_status = rec.credit_limit * 1.1

    @api.onchange('credit_limit')
    def _onchange_credit_limit(self):
        self.credit_limit_status = self.credit_limit * 1.1