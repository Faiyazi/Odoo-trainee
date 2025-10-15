from odoo import models, api


class MailThread(models.AbstractModel):
    _inherit = 'mail.thread'

    @api.model
    def message_post(self, **kwargs):
        msg_vals = kwargs.copy()
        print("_____________msg_vals_________________", msg_vals)

        partner_ids = msg_vals.get('partner_ids', [])
        print("______________partner_ids_____________", partner_ids)

        subtype_xmlid = msg_vals.get('subtype_xmlid')
        print("_________________subtype_xmlid________________", subtype_xmlid)

        # Detect if Log Note
        is_log_note = subtype_xmlid == 'mail.mt_note'
        print("is_log_note", is_log_note)

        # Separate partners into restricted and normal
        normal_partners = []
        restricted_partners = []

        for partner in self.env['res.partner'].browse(partner_ids):
            if partner.restrict_mail:
                restricted_partners.append(partner.id)
            else:
                normal_partners.append(partner.id)

        print("________________normal_partners__________", normal_partners)
        print("_____________restricted_partners____________", restricted_partners)

        # Decide final recipients
        if is_log_note:
            msg_vals['partner_ids'] = normal_partners + restricted_partners
        else:
            msg_vals['partner_ids'] = normal_partners


        return super(MailThread, self).message_post(**msg_vals)
