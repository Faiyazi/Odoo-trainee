import io
import base64
import pandas as pd
from odoo import models, fields


class SaleExcelWizard(models.TransientModel):
    _name = "sale.excel.wizard"
    _description = "Sale Excel Wizard"

    excel_file = fields.Binary(string="Excel file")

    def action_export_excel(self):
        file_content = base64.b64decode(self.excel_file)
        t1 = io.BytesIO(file_content)
        sheet = pd.read_excel(t1)
        print(sheet)

        sale_order = self.env['sale.order'].browse(self.env.context.get('active_id'))
        print("\n\n\n\n\n-------->sale",sale_order)

        # for _,row in sheet.iterrows():
        #     product_name = row[0]
        #     qty = row[1]
        #     price = row[2]
        #     print("\n\n\n\n==============aaaaaaaaaaa",row)

        for index, row in sheet.iterrows():  # pandas way
            product_name = row[0]
            qty = row[1]
            price = row[2]

            qty = float(qty) if pd.notna(qty) else 0.0
            price = float(price) if pd.notna(price) else 0.0

       
            if not product_name:
                continue

            product = self.env['product.product'].search([('name', '=', product_name)], limit=1)
            print("\n\n\n\n-------->product",product)

            if not product:
                product_tmpl = self.env['product.template'].create({
                    'name': product_name,
                    'type': 'consu',
                    # 'list_price': '1',
                })
                product = product_tmpl.product_variant_id


            line = sale_order.order_line.filtered(lambda l: l.product_id == product)

            if line:
                line.write({
                'product_uom_qty': line.product_uom_qty + qty,
                'price_unit': price or line.price_unit,
            })


            else:
                self.env['sale.order.line'].create({
                    'order_id': sale_order.id,
                    'product_id': product.id,
                    'product_uom_qty': qty or 1,
                    'price_unit': price or product.list_price,
                })
