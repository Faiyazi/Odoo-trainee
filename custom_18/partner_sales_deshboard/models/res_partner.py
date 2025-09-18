from odoo import models, fields


class ResPartner(models.Model):
    _inherit = 'res.partner'


    total_sales = fields.Float(string='Total Sales')
    last_sale_date = fields.Datetime(string='Last Sale Date')
    open_invoice_count = fields.Integer(string='Open Invoices')
    top_products = fields.Char(string='Top Products')

    