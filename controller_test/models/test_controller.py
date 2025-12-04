from odoo import models, fields, api


class TestController(models.Model):
    _name = "test.controller"
    _description = "Test Controller"

    name = fields.Char(string="Name")
    price = fields.Float(string="Price")
    discount = fields.Float(string="Discount")
    total = fields.Float(string="Total", compute="compute_total_price")
    image_128 = fields.Binary(string="Image")
    is_published = fields.Boolean("Published", default=False)
  
    
    def action_publish_to_website(self):
        for rec in self:
            rec.is_published = True
        return True

    def action_unpublish_from_website(self):
        for rec in self:
            rec.is_published = False
        return True

    
    

    @api.depends('price', 'discount')
    def compute_total_price(self):
        for rec in self:
            rec.total = rec.price - (rec.price * rec.discount) / 100


class TestPurchaseLog(models.Model):
    _name = "test.purchase.log"
    _description = "Purchase Log"

    product_name = fields.Char(string="Product")
    name = fields.Many2one('res.users', string="Purchased By")
    price = fields.Float(string="Price")
    date = fields.Datetime(string="Date", default=fields.Datetime.now)
