from odoo import models, fields, api, _
from odoo.exceptions import UserError
import base64
import xlrd
import openpyxl
import io


class SaleWizard(models.TransientModel):
    _name = 'sale.wizard'
    _description = 'sale order line wizard through added'

    order_id = fields.Many2one('sale.order', string="Sale Order")
    importfile = fields.Binary(string="Add File:", )

    def action_open_wizard(self):

        self.ensure_one()
        sale_order = self.env['sale.order'].browse(self.env.context.get('active_id'))

        if not sale_order or not self.importfile:
            raise UserError(_("No Sale Order found or file missing."))

        try:
            data = base64.b64decode(self.importfile)
            workbook = openpyxl.load_workbook(io.BytesIO(data))
            sheet = workbook.active

        except Exception as e:
            raise UserError(_("Error reading Excel file: %s") % str(e))

        for row in sheet.iter_rows(min_row=2, values_only=True):  # Skip header
            if not row or len(row) < 3:
                continue

            product_name, qty, price = row
            if not product_name or qty is None or price is None:
                continue
            qty = float(qty)
            price = float(price)

            product = self.env['product.product'].search([('name', '=', product_name)], limit=1)
            if not product:
                product = self.env['product.product'].create({'name': product_name})

                line = sale_order.order_line.filtered(lambda l: l.product_id == product)
                if line:
                    line.product_uom_qty += qty
                else:
                    self.env['sale.order.line'].create({
                        'order_id': sale_order.id,
                        'product_id': product.id,
                        'product_uom_qty': qty,
                        'price_unit': price,
                    })
