from odoo import http
from odoo.http import request


class WebsiteCrmLead(http.Controller):

    @http.route('/crm/lead', type='http', auth='public', website=True)
    def crm_lead(self, **kw):
       
        return request.render("website_crm_lead.lead_form")

    @http.route('/crm/lead/submit', type='http', auth='public', website=True, methods=['GET', 'POST'], csrf=False)
    def crm_lead_form_submit(self, **post):
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

        # request.env['crm.lead'].sudo().create({
        #     'name': name,
        #     'partner_id': partner_id,
        #     'email_from': email,
        #     'phone': phone,
        #     'expected_revenue': expected_revenue,
        #    'probability': probability,
        #     })
        

        # second way in this way use same field name which are in crm.lead e.g. email_from

        # request.env['crm.lead'].sudo().create(kw)

        return request.render('website_crm_lead.lead_form_thankyou')



       
