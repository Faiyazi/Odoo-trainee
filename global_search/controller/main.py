from odoo import http
from odoo.http import request

class GlobalSearchController(http.Controller):

    @http.route('/global_search/search', type='jsonrpc', auth='user')
    def global_search(self, query='', **kw):
        query = query.strip()
        if not query or len(query) < 2:
            return {"result": []}

        results = []
        models = request.env['ir.model'].sudo().search([
            ('transient', '=', False),
            ('model', 'not in', ['ir.logging', 'bus.bus', 'mail.message'])
        ])

        for model_rec in models:
            model_name = model_rec.model
            ModelObj = request.env[model_name].sudo()
            
            if not ModelObj.check_access_rights('read', raise_exception=False):
                continue

            try:
                search_results = ModelObj.name_search(name=query, operator='ilike', limit=5)
                
                for res_id, name in search_results:
                    results.append({
                        "id": res_id,
                        "model": model_name,
                        "display_name": name,
                        "model_label": model_rec.name,
                    })
            except Exception:
                continue

            if len(results) >= 50:
                break

        return {"result": results}