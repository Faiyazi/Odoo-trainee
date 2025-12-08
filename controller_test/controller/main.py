from odoo import http
from odoo.http import request
import base64


class TestControllerOn(http.Controller):

    @http.route('/test', type='http', auth='public', website=True)
    def practice(self, **kw):
        return request.render("controller_test.test_controller_template")

    @http.route('/test/submit/button', type='http', auth='public',
                website=True, methods=['POST'], csrf=False)
    def submit_button_click(self, **post):

        name = post.get('name')
        price = float(post.get('price', 0))
        discount = float(post.get('discount', 0))
        stock = int(post.get('stock', 0))

        image_file = request.httprequest.files.get('image_128')
        image_base64 = False

        image_base64 = base64.b64encode(image_file.read())

        product = request.env['test.controller'].sudo().search(
            [('name', '=', name)], limit=1
        )

        values = {
            'name': name,
            'price': price,
            'discount': discount,
            'stock': stock,
            'image_128': image_base64,
        }
        
        pdf_test,_ = request.env['ir.actions.report'].sudo()._render_qweb_pdf('controller_test.test_controller_template_report',[product.id])
        
        attachment = request.env['ir.attachment'].sudo().create({
            'name':f'Test Product {product.name}',
            'type':'binary',
            'datas':base64.b64encode(pdf_test).decode('utf-8'),
            'res_model': 'test.controller',
            'res_id': product.id,
            'mimetype': 'application/pdf',
            'public': True,
        })
        product.write({
            'attachment_id':attachment,
        })
        
        mail_template = self.env.ref('controller_test.mail_template_test_controller').sudo()
        mail_template.send_mail(product.id, force_send=True, email_values={
        'attachment_ids': [(4, attachment.id)]
        })

        if product:
            product.write(values)
        else:
            request.env['test.controller'].sudo().create(values)

        return request.redirect("/lead/thankyou")

    @http.route('/lead/thankyou', type="http", website=True, auth="public")
    def lead_thank_you(self, **kw):
        return request.render('controller_test.lead_created_template')
