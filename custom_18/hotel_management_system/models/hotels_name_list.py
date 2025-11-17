from odoo import models, fields


class HotelName(models.Model):
    _name = 'hotel.name'
    _description = 'Hotels Name List'

    name = fields.Char(string='Name', help='Enter the full name')
    location = fields.Char(string='Location')
    image = fields.Binary(string='Hotel Image')
    rate = fields.Integer(string='Price')
    hotel_room_ids = fields.One2many('hotel.room', 'hotel_list_id')