from odoo import http
from odoo.http import request

class HotelWebsite(http.Controller):

    @http.route("/hotel/search", type="http", auth="public", website=True)
    def hotel_search(self, **kw):
        return request.render("hotel_management.search_template", {})

    @http.route("/hotel/availability", type="json", auth="public", methods=["POST"])
    def availability_json(self, checkin, checkout, adults=1, children=0):
        Room = request.env["hotel.room"].sudo()
        available = Room.search([("state","=","available")]).mapped("name")
        return {"rooms": available}

    @http.route("/hotel/book", type="http", auth="public", methods=["POST"], csrf=False)
    def hotel_book(self, **post):
        partner = request.env["res.partner"].sudo().create({
            "name": post.get("name"),
            "email": post.get("email"),
        })
        room = request.env["hotel.room"].sudo().search([("state","=","available")], limit=1)
        request.env["hotel.reservation"].sudo().create({
            "partner_id": partner.id,
            "room_id": room.id if room else False,
            "checkin": post.get("checkin"),
            "checkout": post.get("checkout"),
            "adults": int(post.get("adults", 1)),
            "children": int(post.get("children", 0)),
        })
        return request.redirect("/my/hotel/reservations")
