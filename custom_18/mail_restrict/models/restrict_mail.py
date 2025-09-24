from odoo import models, fields

class RestrictMail(models.AbstractModel):
    _inherit = 'mail.thread'


    def _notify_get_recipients(self,message,msg_vals,**kwargs):

        mails = super(RestrictMail, self)._notify_get_recipients(message, msg_vals, **kwargs)

        fil_mails =[]

        for mail in mails:
            partner = mail.get('partner')
            if partner and not partner.restrict_mail:
                fil_mails.append(mail)

        return fil_mails


