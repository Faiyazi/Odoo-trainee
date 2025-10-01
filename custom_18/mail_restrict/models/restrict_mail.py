from odoo import models, fields
from odoo.exceptions import UserError


class RestrictMail(models.AbstractModel):
    _inherit = 'mail.thread'

    def _notify_get_recipients(self, message, msg_vals, **kwargs):

        mails = super()._notify_get_recipients(message, msg_vals, **kwargs)
        print("__________________mails_________", mails)

        rest_true_ids = self.env['res.partner'].search([('restrict_mail', '=', True)]).ids
        print("___________Restricted IDs____________:", rest_true_ids)

        send_mail_allow = []

        for mail in mails:
            partner_id = mail.get('id')
            if partner_id not in rest_true_ids:
                send_mail_allow.append(mail)

        print("___________Allowed recipients:___________", send_mail_allow)

        return send_mail_allow

