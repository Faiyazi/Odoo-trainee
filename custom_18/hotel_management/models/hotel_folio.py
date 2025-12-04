from odoo import api, fields, models, _

class HotelFolio(models.Model):
    _name = "hotel.folio"
    _description = "Hotel Folio"
    _inherit = ["mail.thread", "mail.activity.mixin"]

    name = fields.Char(default=lambda s: s.env["ir.sequence"].next_by_code("hotel.folio"), readonly=True, copy=False)
    reservation_ids = fields.One2many("hotel.reservation", "folio_id")
    line_ids = fields.One2many("hotel.folio.line", "folio_id")
    amount_untaxed = fields.Monetary(compute="_compute_amounts", store=True)
    amount_total = fields.Monetary(compute="_compute_amounts", store=True)
    currency_id = fields.Many2one("res.currency", default=lambda s: s.env.company.currency_id)
    invoice_id = fields.Many2one("account.move", readonly=True)
    payment_state = fields.Selection(related="invoice_id.payment_state", store=True)

    @api.depends("line_ids.price_subtotal")
    def _compute_amounts(self):
        for folio in self:
            subtotal = sum(folio.line_ids.mapped("price_subtotal"))
            folio.amount_untaxed = subtotal
            folio.amount_total = subtotal

    def action_create_invoice(self):
        self.ensure_one()
        move_vals = {
            "move_type": "out_invoice",
            "partner_id": self.reservation_ids[:1].partner_id.id if self.reservation_ids else False,
            "invoice_line_ids": [(0,0,{
                "name": line.description or line.product_id.display_name,
                "product_id": line.product_id.id,
                "quantity": line.quantity,
                "price_unit": line.price_unit,
                "tax_ids": [(6,0,line.tax_ids.ids)]
            }) for line in self.line_ids],
        }
        move = self.env["account.move"].create(move_vals)
        self.invoice_id = move.id
        return {
            "type": "ir.actions.act_window",
            "name": _("Invoice"),
            "res_model": "account.move",
            "view_mode": "form",
            "res_id": move.id,
        }


class HotelFolioLine(models.Model):
    _name = "hotel.folio.line"
    _description = "Hotel Folio Line"

    description = fields.Char()
    reservation_id = fields.Many2one("hotel.reservation")
    folio_id = fields.Many2one("hotel.folio", required=True)
    product_id = fields.Many2one("product.product")
    quantity = fields.Float(default=1.0)
    price_unit = fields.Monetary(currency_field="currency_id")
    tax_ids = fields.Many2many("account.tax")
    price_subtotal = fields.Monetary(compute="_compute_subtotal", store=True)
    currency_id = fields.Many2one(related="folio_id.currency_id", store=True, readonly=True)

    @api.depends("quantity","price_unit","tax_ids")
    def _compute_subtotal(self):
        for l in self:
            l.price_subtotal = (l.quantity or 0.0) * (l.price_unit or 0.0)
