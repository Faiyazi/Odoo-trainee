from odoo import api, fields, models

class HotelAmenity(models.Model):
    _name = "hotel.amenity"
    _description = "Hotel Amenity"
    _inherit = ["mail.thread", "mail.activity.mixin"]

    name = fields.Char(required=True, tracking=True)
    product_id = fields.Many2one("product.product", help="Link to a product if billable")


class HotelRoomType(models.Model):
    _name = "hotel.room.type"
    _description = "Hotel Room Type"
    _inherit = ["mail.thread", "mail.activity.mixin"]

    name = fields.Char(required=True, tracking=True)
    default_rate = fields.Monetary(currency_field="currency_id", tracking=True)
    beds = fields.Integer(default=1, tracking=True)
    description = fields.Text()
    image_1920 = fields.Image()
    currency_id = fields.Many2one("res.currency", default=lambda s: s.env.company.currency_id)


class HotelRoom(models.Model):
    _name = "hotel.room"
    _description = "Hotel Room"
    _inherit = ["mail.thread", "mail.activity.mixin"]

    name = fields.Char(required=True, tracking=True)
    room_type_id = fields.Many2one("hotel.room.type", required=True, tracking=True)
    state = fields.Selection([
        ("available","Available"),
        ("occupied","Occupied"),
        ("dirty","Dirty"),
        ("maintenance","Maintenance"),
    ], default="available", tracking=True)
    capacity = fields.Integer(default=2, tracking=True)
    floor = fields.Integer()
    amenity_ids = fields.Many2many("hotel.amenity", string="Amenities")
    barcode = fields.Char()
