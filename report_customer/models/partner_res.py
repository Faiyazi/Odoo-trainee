from odoo import models


class ResPartner(models.Model):
    _inherit = 'res.partner'

    def action_print_report_pdf(self):
        print('hello')
        customers = self.env['res.partner'].search([])
        print(customers)

        company = self.env['res.company'].browse(1)  # Usually ID=1 for your main company

        # Print the logo (base64 string)
        print(company.logo)
        return self.env.ref('report_customer.report_customer_action').report_action(customers)
