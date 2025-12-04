from odoo import models

class MailThread(models.AbstractModel):
    _inherit = 'mail.thread'

    def _notify_get_recipients(self, records, msg_vals=None):   
        print("\n\n\n\n---------->self", self)
        print("\n\n----------->records", records)
        print("\n\n\n----------->msg", msg_vals)

        recipients = super()._notify_get_recipients(records, msg_vals=msg_vals)
        print("\n\n------->recipients", recipients)

        data = []
        print("\n\n------------>data", data)

        # Get list of explicitly mentioned partner IDs (via @)
        mentioned_ids = set(msg_vals.get('partner_id', [])) if msg_vals else set()

        for record in recipients:
            partners_id = record.get('id')  # This is probably wrong in original, see note below
            print("\n\n\n\n----------->partners", partners_id)

            if partners_id:
                partner = self.env['res.partner'].browse(partners_id)
                print("\n\n\n--------->partner", partner)

                # Only block if restrict_mail=True and partner not mentioned
                if partner and not (partner.restrict_mail and partner.id not in mentioned_ids):
                    data.append(record)
                else:
                    print("[BLOCKED] {partner.name} is restricted follower (no @ mention)")

        return data
