from odoo import models, api
from odoo.exceptions import ValidationError, UserError


class MailThread(models.AbstractModel):
    _inherit = 'mail.thread'
    

    @api.model

    def _notify_get_recipients(self, message, msg_vals, **kwargs):
        recipients = super()._notify_get_recipients(message, msg_vals, **kwargs)

        # Filter recipients: exclude partners with restrict_mail = True
        restricted_ids = set(
            self.env['res.partner'].search([('restrict_mail', '=', True)]).ids
        )

        for r in recipients:
            if restricted_ids and not r.get('partner_id'):
                raise UserError('its restricted')

        filtered = [
            r for r in recipients
            if not r.get('partner_id') in restricted_ids
        ]
        return filtered


