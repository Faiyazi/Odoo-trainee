from odoo import models, fields
from odoo.exceptions import UserError
import base64
import tempfile
import openpyxl

class SaleOrderWizard(models.TransientModel):
    _name= 'sale.order.wizard'
    _description = 'Sale Order Wizard'


    file = fields.Binary(string="Excel File")
    sale_id = fields.Many2one('sale.order', string='Sale Order', readonly=True)
    


    def action_import(self):
        if not self.file:
            raise UserError("Please upload an Excel file.")
        

        data = base64.b64decode(self.file)
        temp = tempfile.NamedTemporaryFile(delete=False, suffix=".xlsx")
        temp.write(data)
        temp.seek(0)

        try:
            workbook = openpyxl.load_workbook(temp.name)
            print("\n\n\n-------->gggggggg",workbook)
            sheet = workbook.active
            print("\n\n\n------------>sheet",sheet)
        except Exception:
            print("\n\n\n-------------asdasdasdasdasdasd")
            raise UserError("Invalid Excel file format!")


        sale_order = self.env['sale.order'].browse(self.env.context.get('active_id'))
        print("\n\n\n-------------->sale_order",sale_order)
        if not sale_order:
            raise UserError("No Sale Order found.")

        orderline_obj = self.env['sale.order.line']
        
        for row in sheet.iter_rows(min_row=2, values_only=True):
            print("\n\n\n\n------------>row",row)
            product_id, qty, price = row[0], row[1], row[2]

            if not product_id:
                continue

            product = self.env['product.product'].search([('name', '=', product_id)], limit=1)
            print("\n\n\n\n------------>product",product)

            if not product:
                
                product = self.env['product.template'].create({
                                        'name': product_id,
                                    })

            existing_line = sale_order.order_line.filtered(lambda o: o.product_id == product)
            print("\n\n\n\n\n-------------->existing_line",existing_line)

            if existing_line:
                existing_line.product_uom_qty += qty or 0
                if price:
                    existing_line.price_unit = price
            else:
                orderline_obj.create({
                    'order_id': sale_order.id,
                    'product_id': product.id,
                    'product_uom_qty': qty or 1,
                    'price_unit': price or product.list_price,
                })

        return 
