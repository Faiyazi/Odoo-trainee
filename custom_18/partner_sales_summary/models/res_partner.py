from odoo import models, fields


class ResPartner(models.Model):
    _inherit = 'res.partner'

    total_sales = fields.Float(string='Total Sales')


    def update_total_sales(self):

        customers = self.env['res.partner'].search([('customer_rank', '>', 0)])

        if not customers:
            return
        
        partner_ids = customers.ids
        print("\n\n\n\n\n==================>",partner_ids)
        
        self.env.flush_all()


        self.env.cr.execute("""
            SELECT partner_id, SUM(amount_total) AS total
            FROM sale_order
            WHERE state='sale'
            AND partner_id= ANY(%s)
            GROUP BY partner_id
        """, [partner_ids])

        totals = dict(self.env.cr.fetchall())

        for partner in customers:
            partner.total_sales = totals.get(partner.id, 0.0)

        return True