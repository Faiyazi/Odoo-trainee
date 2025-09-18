from odoo import models

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    def _notify_get_recipients(self, records, msg_vals=None):   
        print("\n\n\n\n---------->self", self)
        print("\n\n----------->records", records)
        print("\n\n\n----------->msg", msg_vals)

        recipients = super()._notify_get_recipients(records, msg_vals=msg_vals)
        print("\n\n------->recipients", recipients)

        data = []
        print("\n\n------------>data", data)
        
        for record in recipients:
            
            partners_id = record.get('id')
            print("\n\n\n\n----------->partners",partners_id)

            if partners_id:
                partner =self.env['res.partner'].browse(partners_id)
                print("\n\n\n--------->partner",partner)
                if partner and not partner.restrict_mail:
                    data.append(record)
                    
        return data




