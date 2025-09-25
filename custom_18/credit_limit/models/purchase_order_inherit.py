from odoo import models, fields, api


class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    state = fields.Selection(selection_add=[
        ('first_approval','First Approval'),
        ('second_approval','Second Approval')
    ])

    def button_confirm(self):
        get_limit_settings = float(self.env['ir.config_parameter'].sudo().get_param('credit_limit'))
        print("__________________________",get_limit_settings)
        for order in self:
            get_contact_limit = float(order.partner_id.partner_credit_limit)
            print("________________________________",get_contact_limit,)
            if get_contact_limit > get_limit_settings :
                order.state = 'first_approval'
            # else:
            #      order.state = 'second_approval'

        return super(PurchaseOrder, self).button_confirm()

    def action_first_approval(self):
        for order in self:
            order.state = 'second_approval'

    def action_second_approval(self):
        for order in self:
            order.state = 'purchase'
