from odoo import http
from odoo.http import request


class TestControllerOn(http.Controller):
    @http.route('/test' ,type='http', auth='public',website=True)

    def practice(self, **kw):
        print("\n\n\n\n\n\n\n============================>")
        # details = request.env['test.controller'].sudo().search([])
       
        return request.render("controller_test.test_controller_template")

    @http.route('/test/submit/button', type='http', auth='public', website=True, methods=['GET', 'POST'], csrf=False)
    def submit_button_click(self, **post):
        print("aaaaaaaaaaa")

        # # first way
        
        # name = post.get('name')
        # print("\n\n\n------------",name)
        # partner_id = post.get('partner_id')
        # print("\n\n\n------>dd",partner_id)
        # email = post.get('email')
        # phone = post.get('phone')
        # expected_revenue = post.get('expected_revenue')
        # probability = post.get('probability')

        request.env['test.controller'].sudo().create({
            'name': post.get('name'),
            'price': post.get('price'),
            'discount': post.get('discount'),
            'image_128': post.get('image_128'), 
            })
        
        

        # # second way in this wty use same field name which are in crm.lead e.g. email_from

        # request.env['crm.lead'].sudo().create(kw)

        return request.redirect("/lead/thankyou")
    
    
    @http.route('/lead/thankyou', type="http", website=True, auth="public")
    def lead_thank_you(self, **kw):
        return request.render('controller_test.lead_created_template')