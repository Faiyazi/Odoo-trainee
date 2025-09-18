from odoo import api, fields, models, _
from odoo.exceptions import ValidationError

class HotelReservation(models.Model):
    _name = "hotel.reservation"
    _description = "Hotel Reservation"
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _order = "checkin desc, id desc"

    name = fields.Char(default=lambda s: s.env["ir.sequence"].next_by_code("hotel.reservation"), readonly=True, copy=False)
    partner_id = fields.Many2one("res.partner", required=True, tracking=True)
    room_id = fields.Many2one("hotel.room", required=True, tracking=True)
    checkin = fields.Datetime(required=True, tracking=True)
    checkout = fields.Datetime(required=True, tracking=True)
    adults = fields.Integer(default=1)
    children = fields.Integer(default=0)
    state = fields.Selection([
        ("draft","Draft"),("confirmed","Confirmed"),("checkin","Checked In"),
        ("checkout","Checked Out"),("cancel","Cancelled")
    ], default="draft", tracking=True)
    rate_plan_id = fields.Many2one("hotel.rate.plan")
    price_subtotal = fields.Monetary(compute="_compute_amounts", store=True)
    price_total = fields.Monetary(compute="_compute_amounts", store=True)
    currency_id = fields.Many2one("res.currency", default=lambda s: s.env.company.currency_id)
    folio_id = fields.Many2one("hotel.folio")
    service_line_ids = fields.One2many("hotel.folio.line", "reservation_id")

    @api.constrains("checkin","checkout","room_id")
    def _check_dates_and_overlap(self):
        for r in self:
            if r.checkout and r.checkin and r.checkout <= r.checkin:
                raise ValidationError(_("Checkout must be after checkin."))
            if not r.room_id or not r.checkin or not r.checkout:
                continue
            domain = [
                ("id","!=",r.id),
                ("room_id","=",r.room_id.id),
                ("state","in",["confirmed","checkin"]),
                ("checkin","<",r.checkout),
                ("checkout",">",r.checkin),
            ]
            if self.search_count(domain):
                raise ValidationError(_("Room is not available in the selected period."))

    @api.depends("checkin","checkout","rate_plan_id","adults","children")
    def _compute_amounts(self):
        for r in self:
            if not (r.checkin and r.checkout and r.rate_plan_id):
                r.price_subtotal = r.price_total = 0.0
                continue
            nights = (fields.Date.to_date(r.checkout) - fields.Date.to_date(r.checkin)).days
            base = r.rate_plan_id.base_price * nights
            extra = max(r.adults-2, 0) * (r.rate_plan_id.extra_adult_price or 0.0) * nights
            child = (r.children or 0) * (r.rate_plan_id.child_price or 0.0) * nights
            factor = r.rate_plan_id.season_id.pricing_factor or 1.0
            subtotal = (base + extra + child) * factor
            r.price_subtotal = subtotal
            r.price_total = subtotal

    def action_confirm(self):
        for r in self:
            r.state = "confirmed"
            r.message_post(body=_("Reservation confirmed."))

    def action_checkin(self):
        for r in self:
            if fields.Datetime.now() < r.checkin:
                raise ValidationError(_("Cannot check-in before check-in time."))
            r.state = "checkin"
            r.room_id.state = "occupied"
            r.message_post(body=_("Guest checked in."))

    def action_checkout(self):
        for r in self:
            r.state = "checkout"
            r.room_id.state = "dirty"
            self.env["hotel.housekeeping.task"].create({
                "name": _("Clean: %s") % r.room_id.name,
                "room_id": r.room_id.id,
                "assigned_user_id": False,
                "date": fields.Date.today(),
            })
            r.message_post(body=_("Checked out; housekeeping task created."))
