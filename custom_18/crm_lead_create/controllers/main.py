from odoo import http,fields,models
from odoo.http import request


class CreateFormToLead(http.Controller):
    @http.route('/lead', type="http",website=True, auth="public")
    def lead_form_show(self, **kwargs):
        customer_name = request.env['res.partner'].sudo().search([])

        return request.render('crm_lead_create.crm_lead_template',{
            'customer_name':customer_name
        })

    @http.route('/lead/submit_button', type="http", auth="public", website=True, methods=['POST'],csrf=False)
    def submit_button_click(self, **post):
        lead = request.env['crm.lead'].sudo().create({
            'name': post.get('name'),
            'email_from': post.get('email'),
            'partner_id': post.get('partner_id') or False,
            'phone': post.get('phone'),
            'probability': float(post.get('probability')),
            'expected_revenue': float(post.get('expected_revenue')),
        })
        return request.redirect("/lead")
