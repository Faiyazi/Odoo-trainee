from odoo import api, fields, models, _
from odoo.exceptions import ValidationError

class HotelCheckinWizard(models.TransientModel):
    _name = "hotel.checkin.wizard"
    _description = "Check-In Wizard"

    reservation_id = fields.Many2one("hotel.reservation", required=True)
    deposit_amount = fields.Monetary(currency_field="currency_id", help="Optional deposit to register")
    currency_id = fields.Many2one("res.currency", default=lambda s: s.env.company.currency_id)

    def action_checkin(self):
        self.ensure_one()
        self.reservation_id.action_checkin()
        return {"type": "ir.actions.act_window_close"}
