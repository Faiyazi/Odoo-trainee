from odoo import models, fields, api
from odoo.exceptions import UserError
import io
import xlsxwriter
import base64

class SaleRegisterWizard(models.TransientModel):
    _name = "sale.register.wizard"
    _description = "Sale Register Wizard"

    start_date = fields.Date("Start Date", required=True)
    end_date = fields.Date("End Date", required=True)

    @api.constrains('start_date', 'end_date')
    def _check_dates(self):
        for rec in self:
            if rec.start_date > rec.end_date:
                raise UserError("End Date must be grater than start date.")

    def action_download_excel(self):
        self.ensure_one()

        sale_orders = self.env['sale.order'].search([
            ('date_order', '>=', self.start_date),
            ('date_order', '<=', self.end_date)
        ])

        if not sale_orders:
            raise UserError("No Data Found For That Period !!")

        try:
            # HEADERS
            green_column = [
                "Delivery Number", "Delivery Date/Date Time", "Mantra Sale Order Number", "Sale Order Date",
                "Mantra Inward Number", "Customer PO number", "Invoice Number", "Invoice Date", "Company Name",
                "Branch Name", "Store Code", "Store Name", "Sub Store Location", "Customer Code", "Customer Name",
                "Customer Address", "Movement Code", "Description/Voucher Type", "Voucher Reason", "Narration",
                "Mantra DC No.", "Mantra DC Date", "Material Category", "Material Code", "Variety", "Size", "Generation",
                "Batch Number", "Store Marka/pavti number", "Cold Storage Outward Gatepass number",
                "Dispatch Location weight slip Number (RST)", "Dispatch Location Weight (Kgs)",
                "Receiving Location weight slip Number (RST)", "Receiving Location Weight (Kgs)", "SO Rate",
                "Value as per SO Rate", "Freight Rate", "Freight Value", "Penalty", "Detention", "Re-Location",
                "Pending", "Additional Freight", "Total Freight Cost", "Freight Partner", "GL-Number", "GL-Description",
                "Cost Center Code", "Cost Center Name", "Vessel/Truck Number", "Truck Builty Number",
                "Driver Mobile Number", "Incoterm", "Customer Credit Note No.", "Customer Credit Note Qty",
                "Customer Credit Note Value", "Customer Debit Note No.", "Customer Debit Note Qty",
                "Customer Debit Note Value", "Dispatch Date Time", "Reporting Date Time", "Unloading Date Time",
                "Batch Supplier Code", "Batch Supplier Name"
            ]

            pink_column = [
                "Quality Report Number", "Quality Report Date", "Quality Inspector Name", "under size", "Over Size",
                "Soil in Potato", "Mechanical damage/Cut-Crack", "Scab", "Greening", "Wet rot", "Dry rot", "Infestation",
                "Second Growth/Growth Crack", "Other external Defects", "Black spot on Potato", "Bruising",
                "Fungus Infection", "Other", "Total External Defects Limits"
            ]

            grey_column = [
                "Greening", "Underirable Color", "External Diffect", "Internal Diffect", "Total Product Defect",
                "Type of Packing", "Payment Term", "Customer Quantity GRN Kgs", "Customer Quantity Deduction Kgs",
                "Customer Quantity Value", "Customer Quality Deduction  %", "Customer Quality Deduction  Value",
                "Total Deduction"
            ]

            headers = green_column + pink_column + grey_column

            # PREPARE WORKBOOK
            output = io.BytesIO()
            workbook = xlsxwriter.Workbook(output, {'in_memory': True})
            sheet = workbook.add_worksheet("Sale-Outward Register")
            center_format = workbook.add_format({'align': 'center', 'valign': 'vcenter','text_wrap': True ,
                                                 'font_size': 10, 'font_name': 'Arial'})

            # Title
            title_format = workbook.add_format({'bold': True, 'font_size': 18, 'align': 'center', 'valign': 'vcenter'})
            sheet.merge_range(2, 0, 2, len(headers) - 1, "Sale-Outward Register", title_format)
            sheet.set_row(2, 20)
            sheet.set_row(5, 45)

            # Header formatting
            green_fmt = workbook.add_format({'bold': True, 'bg_color': '#92D050', 'border': 1,'font_name': 'Arial',
                                             'align': 'center', 'valign': 'vcenter', 'text_wrap': True, 'font_size': 10})
            pink_fmt = workbook.add_format({'bold': True, 'bg_color': '#FFC0CB', 'border': 1,'font_name': 'Arial',
                                            'align': 'center', 'valign': 'vcenter', 'text_wrap': True, 'font_size': 10})
            grey_fmt = workbook.add_format({'bold': True, 'bg_color': '#D9D9D9', 'border': 1,'font_name': 'Arial',
                                            'align': 'center', 'valign': 'vcenter', 'text_wrap': True, 'font_size': 10})

            # Write headers
            header_row = 5
            col = 0
            for h in green_column: sheet.write(header_row, col, h, green_fmt); col += 1
            for h in pink_column: sheet.write(header_row, col, h, pink_fmt); col += 1
            for h in grey_column: sheet.write(header_row, col, h, grey_fmt); col += 1

            # Set column widths
            for i in range(col):
                sheet.set_column(i, i, 18)

            row = header_row + 1

            # Date formatting
            def fmt(dt):
                return dt.strftime("%d-%m-%Y %H:%M:%S") if dt else ""

            for rec in sale_orders:
                partner = rec.partner_id
                company = rec.company_id

                # Invoices
                invoice = self.env['account.move'].search([
                    ('invoice_origin', '=', rec.name),
                    ('name', '=like', 'INV%'),
                ])

                # Credit/Debit Notes
                credit_notes = self.env['account.move'].search([('invoice_origin', '=', rec.name),
                                                                  ('move_type', '=', 'out_refund')])
                debit_notes = self.env['account.move'].search([('invoice_origin', '=', rec.name),
                                                                 ('name', 'ilike', 'DINV')])

                credit_note_no = ", ".join(credit_notes.mapped('name')) or ""
                credit_note_qty = sum(credit_notes.mapped('invoice_line_ids.quantity') or [0])
                credit_note_value = sum(credit_notes.mapped('amount_total') or [0.0])

                debit_note_no = ", ".join([str(n) for n in debit_notes.mapped('name') if n]) or ""
                debit_note_qty = sum(debit_notes.mapped('invoice_line_ids.quantity') or [0])
                debit_note_value = sum(debit_notes.mapped('amount_total') or [0.0])

                for line in rec.order_line:
                    product = line.product_id.product_tmpl_id if line.product_id else False
                    grn_weight = sum(line.move_ids.mapped('quantity'))
                    so_rate = line.price_unit
                    grn_value = grn_weight * so_rate
                    freight_rate = sum(line.move_ids.mapped('freight_fees'))
                    freight_value = freight_rate * line.product_uom_qty

                    pickings = line.move_ids.mapped("picking_id")

                    for picking in pickings:

                        dispatch = picking.dispatch_id if picking else False

                        # supplier from dispatch
                        supplier_code = dispatch.supplier_code if dispatch else ""
                        supplier_name = dispatch.supplier_id.name if dispatch and dispatch.supplier_id else ""

                        location = line.move_ids[:1].location_id if line.move_ids else False

                        qc = self.env['quality.check'].search([
                            ('picking_id', '=', picking.id),
                            ('product_id', '=', line.product_id.id),
                        ], order='id desc', limit=1)

                        if not qc:
                            qc = False

                        # Sampling lines
                        sampling_lines = self.env['quality.sampling.line'].search(
                            [('quality_check_id', '=', qc.id)]) if qc else self.env['quality.sampling.line']

                        sampling_fields = ['us', 'os', 'sm', 'md', 'scab', 'green', 'wet_rot', 'dry_rot', 'infection',
                                           'sg', 'bs', 'brusing', 'fi', 'others']
                        sampling_avg = {
                            f: (sum(sampling_lines.mapped(f)) / len(sampling_lines)) if sampling_lines else 0 for f in
                            sampling_fields
                        }

                        # Cooktest lines
                        cook_lines = self.env['quality.cooktest.line'].search(
                            [('quality_check_id', '=', qc.id)]) if qc else self.env['quality.cooktest.line']
                        cook_fields = ['uc', 'ed', 'qcl_id', 'tpod']
                        cook_avg = {f: (sum(cook_lines.mapped(f)) / len(cook_lines)) if cook_lines else 0 for f in
                                    cook_fields}

                        # Build row
                        row_values = [
                            picking.name if picking else "",                        # Delivery Number
                            fmt(picking.date_done) if picking else "",              # Delivery Date/Date Time
                            rec.name,                                               # Mantra Sale Order Number
                            fmt(rec.date_order),                                    # Sale Order Date
                            picking.name if picking else "",                        # Mantra Inward Number
                            "",                                                     # Customer PO number
                            invoice.name  if invoice else "",                       # Invoice Number
                            fmt(invoice.invoice_date)if invoice else "",            # Invoice Date
                            company.name if company else "",                        # Company Name
                            partner.branch_code or "",                              # Branch Name
                            location.sequence if location else "",                  # Store Code
                            location.name if location else "",                      # Store Name
                            location.location_id.name if location and location.location_id else "",         # Sub Store Location
                            partner.unique_code or "",                              # Customer Code
                            partner.name or "",                                     # Customer Name
                            partner.city or "",                                     # Customer Address
                            "",                                                     # Movement Code
                            "",                                                     # Description/Voucher Type
                            "",                                                     # Voucher Reason
                            "",                                                     # Narration
                            "",                                                     # Mantra DC No.
                            "",                                                     # Mantra DC Date
                            product.categ_id.complete_name if product else "",      # Material Category
                            product.default_code if product else "",                # Material Code
                            product.variety_id.name if product else "",             # Variety
                            product.size if product else "",                        # Size
                            product.generation if product else "",                  # Generation
                            ", ".join(line.move_ids.mapped("lot_ids.name")) if line.move_ids else "",       # Batch Number
                            ", ".join([str(m) for m in line.move_ids.mapped("lot_ids.marka_number") if m]), # Store Marka/pavti number
                            "",                                                     # Cold Storage Outward Gatepass number
                            "",                                                     # Dispatch Location weight slip Number (RST)
                            "",                                                     # Dispatch Location weight (Kgs)
                            "",                                                     # Receiving Location weight slip Number (RST)
                            "",                                                     # Receiving Location weight (Kgs)
                            so_rate,                                                # SO Rate
                            grn_value,                                              # Value as per SO Rate
                            round(freight_rate, 2),                                 # Freight Rate
                            freight_value,                                          # Freight Value
                            "",                                                     # Penalty
                            "",                                                     # Detention
                            "",                                                     # Re-Location
                            "",                                                     # Pending
                            "",                                                     # Additional Freight
                            "",                                                     # Total Freight Cost
                            dispatch.transporter_id.name if dispatch else "",       # Freight Partner
                            "",                                                     # GL-Number
                            "",                                                     # GL-Description
                            "",                                                     # Cost Center Code
                            "",                                                     # Cost Center Name
                            dispatch.truck_number if dispatch else "",              # Vessel/Truck Number
                            dispatch.transporter_bilty_no if dispatch else "",      # Truck Builty Number
                            dispatch.truck_driver_contact if dispatch else "",      # Driver Mobile Number
                            rec.incoterm.name if rec.incoterm else "",              # Incoterm
                            credit_note_no,                                         # Customer Credit Note No.
                            credit_note_qty,                                        # Customer Credit Note Qty
                            credit_note_value,                                      # Customer Credit Note Value
                            debit_note_no,                                          # Customer Debit Note No.
                            debit_note_qty,                                         # Customer Debit Note Qty
                            debit_note_value,                                       # Customer Debit Note Value
                            "",                                                     # Dispatch Date Time
                            "",                                                     # Reporting Date Time
                            "",                                                     # Unloading Date Time
                            supplier_code,                                          # Batch Supplier Code
                            supplier_name,                                          # Batch Supplier Name
                            # pink_column
                            qc.name if qc else "",                                  # Quality Report Number
                            fmt(qc.control_date) if qc else "",                     # Quality Report Date
                            qc.user_id.name if qc else "",                          # Quality Inspector Name
                            sampling_avg['us'],                                     # Under size
                            sampling_avg['os'],                                     # Over size
                            sampling_avg['sm'],                                     # Soil in Potato
                            sampling_avg['md'],                                     # Mechanical damage/Cut-Crack
                            sampling_avg['scab'],                                   # Scab
                            sampling_avg['green'],                                  # Greening
                            sampling_avg['wet_rot'],                                # Wet rot
                            sampling_avg['dry_rot'],                                # Dry rot
                            sampling_avg['infection'],                              # Infestation
                            sampling_avg['sg'],                                     # Second Growth/Growth Crack
                            "",                                                     # Other external Defects
                            sampling_avg['bs'],                                     # Black spot on Potato
                            sampling_avg['brusing'],                                # Bruising
                            sampling_avg['fi'],                                     # Fungus Infection
                            sampling_avg['others'],                                 # Other
                            "",                                                     # Total External Defects Limits
                            # grey_cloumn
                            "",                                                     # Greening
                            cook_avg['uc'],                                         # Underirable Color
                            cook_avg['ed'],                                         # External Diffect
                            cook_avg['qcl_id'],                                     # Internal Diffect
                            cook_avg['tpod'],                                       # Total Product Defect
                            "",                                                     # Type of Packing
                            rec.payment_term_id.name if rec.payment_term_id else "",# Payment Term
                            grn_weight,                                             # Customer Quantity GRN Kgs
                            "",                                                     # Customer Quantity Deduction Kgs
                            grn_value,                                              # Customer Quantity Value
                            "",                                                     # Customer Quality Deduction %
                            "",                                                     # Customer Quality Deduction Value
                            "",                                                     # Total Deduction
                        ]
                        # Write row
                        for col_idx, val in enumerate(row_values):
                            sheet.write(row, col_idx, val if val is not None else "", center_format)
                            sheet.set_row(row, 22)
                        row += 1

            workbook.close()
            output.seek(0)
            file_data = output.read()

            export_id = self.env['sale.register.excel'].create({
                'excel_file': base64.b64encode(file_data),
                'file_name': f"Sale_Register_{self.start_date}_{self.end_date}.xlsx"
            })

            return {
                'name': "Download Sale Register Report",
                'view_mode': 'form',
                'res_id': export_id.id,
                'res_model': 'sale.register.excel',
                'type': 'ir.actions.act_window',
                'target': 'new',
            }
        except Exception:
            raise UserError("Something went wrong while generating the Excel. Please check your data.")


from odoo import models, fields

class SaleRegisterExcel(models.TransientModel):
    _name = "sale.register.excel"
    _description = "Sale Register Excel"

    excel_file = fields.Binary("Excel Report")
    file_name = fields.Char("File Name")
