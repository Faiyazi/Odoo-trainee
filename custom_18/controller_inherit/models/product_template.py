from odoo import fields, models

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    discount = fields.Float(string='Discount(%)',default=0.0, help="Discount percentage applied to this product.")