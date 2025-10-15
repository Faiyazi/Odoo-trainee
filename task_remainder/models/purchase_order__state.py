from odoo import models, fields


class PurchaseOrderState(models.Model):
    _inherit = 'purchase.order'

    state = fields.Selection(
        selection_add=[
            ('first_approval', 'First Approval'),
            ('second_approval', 'Second Approval'),
        ],
        ondelete={
            'first_approval': 'set default',
            'second_approval': 'set default',
        }
    )

    def button_confirm(self):
        # get global credit setting
        setting_credits = float(
            self.env['ir.config_parameter'].sudo().get_param('custom_task.credit')
        )

        for order in self:
            partner_limit = getattr(order.partner_id, 'partner_credits_limits')

            if partner_limit > setting_credits:
                order.write({'state': 'first_approval'})
            else:
                order.write({'state': 'second_approval'})

        return super().button_confirm()


