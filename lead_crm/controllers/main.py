
from odoo import http
from odoo.http import request


class Practice(http.Controller):

    @http.route('/lead', type="http",website=True, auth="public")
    def practice_task(self, **kw):
        details = request.env['res.partner'].sudo().search([])

        return request.render('lead_crm.crm_leads_template',{
            'details':details
        })

    @http.route('/lead/submit', type="http", auth="public", website=True, methods=['POST'],csrf=False)
    def practice_task_submit(self, **post):
        lead = request.env['crm.lead'].sudo().create({
            'name': post.get('name'),
            'email_from': post.get('email'),
            'partner_id': post.get('partner_id') or False,
            'phone': post.get('phone'),
            'probability': float(post.get('probability')),
            'expected_revenue': float(post.get('expected_revenue')),
        
        })
        return request.redirect("/lead/thankyou")
    
    
    @http.route('/lead/thankyou', type="http", website=True, auth="public")
    def lead_thank_you(self, **kw):
        return request.render('lead_crm.lead_created_template')


