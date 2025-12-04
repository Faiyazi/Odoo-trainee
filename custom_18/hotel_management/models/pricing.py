from odoo import api, fields, models

class HotelSeason(models.Model):
    _name = "hotel.season"
    _description = "Hotel Season"
    _inherit = ["mail.thread", "mail.activity.mixin"]

    name = fields.Char(required=True)
    date_start = fields.Date(required=True)
    date_end = fields.Date(required=True)
    pricing_factor = fields.Float(default=1.0, help="Multiplier applied to base price")


class HotelRatePlan(models.Model):
    _name = "hotel.rate.plan"
    _description = "Hotel Rate Plan"
    _inherit = ["mail.thread", "mail.activity.mixin"]

    name = fields.Char(required=True, tracking=True)
    room_type_id = fields.Many2one("hotel.room.type", required=True)
    season_id = fields.Many2one("hotel.season")
    base_price = fields.Monetary(currency_field="currency_id", required=True)
    extra_adult_price = fields.Monetary(currency_field="currency_id", default=0.0)
    child_price = fields.Monetary(currency_field="currency_id", default=0.0)
    min_stay = fields.Integer(default=1)
    max_stay = fields.Integer()
    currency_id = fields.Many2one("res.currency", default=lambda s: s.env.company.currency_id)
