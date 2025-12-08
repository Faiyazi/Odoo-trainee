from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


class TestController(models.Model):
    _name = "test.controller"
    _description = "Test Controller"

    name = fields.Char(string="Name", required=True)
    price = fields.Float(string="Price", digits=(16, 2), required=True)
    discount = fields.Float(string="Discount (%)", digits=(16, 2))
    total = fields.Float(
        string="Total",
        compute="_compute_total_price",
        store=True,
        digits=(16, 2)
    )
    image_128 = fields.Binary(string="Image")
    stock = fields.Integer(string="Stock", default=0)
    add_to_cart = fields.Integer(string="Add to Cart", default=1)
    is_published = fields.Boolean("Published", default=False)
    attachment_id = fields.Many2one('ir.attachment','Attachment')

    @api.depends('price', 'discount')
    def _compute_total_price(self):
        for rec in self:
            rec.total = rec.price - (rec.price * rec.discount) / 100

class TestPurchaseLog(models.Model):
    _name = "test.purchase.log"
    _description = "Purchase Log"

    product_name = fields.Char(string="Product", required=True)
    name = fields.Many2one('res.users', string="Purchased By", required=True)
    price = fields.Float(string="Price", digits=(16, 2))
    purchase_quantity = fields.Integer(string="Purchase Quantity", default=1)
    date = fields.Datetime(string="Date", default=fields.Datetime.now)
