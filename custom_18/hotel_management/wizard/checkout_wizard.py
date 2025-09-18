from odoo import api, fields, models, _

class HotelCheckoutWizard(models.TransientModel):
    _name = "hotel.checkout.wizard"
    _description = "Check-Out Wizard"

    reservation_id = fields.Many2one("hotel.reservation", required=True)
    folio_id = fields.Many2one(related="reservation_id.folio_id", readonly=True)
    create_invoice = fields.Boolean(default=True)

    def action_checkout(self):
        self.ensure_one()
        self.reservation_id.action_checkout()
        if self.create_invoice and self.folio_id:
            self.folio_id.action_create_invoice()
        return {"type": "ir.actions.act_window_close"}
