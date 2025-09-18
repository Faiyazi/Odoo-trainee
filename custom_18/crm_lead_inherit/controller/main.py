from odoo import http
from odoo.http import request

from odoo.addons.website_crm_lead.controllers.main import WebsiteCrmLead


class WebsiteCrmLeadInherit(WebsiteCrmLead):

    @http.route('/crm/lead/inherit', type='http', auth='public', website=True)
    def crm_lead(self, **kw):
       
        return request.render("crm_lead_inherit.portal_my_orders_inherit")