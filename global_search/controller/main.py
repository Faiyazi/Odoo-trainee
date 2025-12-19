from odoo import http
from odoo.http import request

class GlobalSearchController(http.Controller):

    @http.route('/global_search/search', type='json', auth='user')
    def global_search(self, query='', **kw):
        query = query.strip()
        if not query or len(query) < 2:
            return {"result": []}

        results = []
        # 1. Fetch all models that are not transient/abstract
        # We filter for models that have a name and are actually stored in the DB
        models = request.env['ir.model'].sudo().search([
            ('transient', '=', False),
            ('model', 'not in', ['ir.logging', 'bus.bus', 'mail.message']) # Exclude noise
        ])

        for model_rec in models:
            model_name = model_rec.model
            ModelObj = request.env[model_name].sudo()
            
            # 2. Check if the user has access to this model
            if not ModelObj.check_access_rights('read', raise_exception=False):
                continue

            # 3. Use 'name_search' to find records
            # This is more efficient than manual domain building because it uses 
            # the model's defined search logic (searching name, ref, etc.)
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
                # Some models might have broken name_get/name_search implementations
                continue

            # Stop if we have gathered enough total results to keep performance snappy
            if len(results) >= 50:
                break

        return {"result": results}