from odoo import models

class MailFollowers(models.Model):
    _inherit = 'mail.followers'

    def _get_recipient_data(self, records, message_type, subtype_id, pids=None):
        print("\n\n\n---------->self",self)
        print("\n\n\n---------->records",records)
        print("\n\n\n---------->message",message_type)
        print("\n\n\n------->subtype",subtype_id)
        print("\n\n------------------>pid",pids)

        recipients = super()._get_recipient_data(records, message_type, subtype_id, pids=pids)
        print("\n\n-------> Original recipients:", recipients)

        subtype = self.env['mail.message.subtype'].browse(subtype_id) 
        print("\n\n\n----------->subbbb",subtype)
        subtype_name = subtype.name 
        print("\n\n--------->subtype",subtype_name)
        
        for record in records:

            rec_data = recipients.get(record.id,{})
            print("\n\n\n----------->record",rec_data)

            filtered_recipients = {}

            for partner_id, data in rec_data.items():

                partner = self.env['res.partner'].browse(partner_id)

                print("\n\n\n--------->partner1111",partner)
                      
                if  not partner.restrict_mail:
                    print("\n\n\n---------asdfghjkl")
                    filtered_recipients[partner_id] = data
                    print("\n\n=------------>aaaaaa",filtered_recipients[partner_id])
                    continue

                if subtype_name == "Note":
                    filtered_recipients[partner_id] = data
                    print("\n\n--------->bbbbbb",filtered_recipients[partner_id])
                    continue
                
                continue
            recipients[record.id]= filtered_recipients

        print("\n\n-------> Filtered recipients:", recipients[record.id])
        return recipients
