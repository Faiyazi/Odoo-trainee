from odoo import models, fields, api

class NewObject(models.Model):
    _name = "new.object"
    _description = "New Object with Name Field"

    name = fields.Char(string="Name", required=True)

    _sql_constraints = [
        ('unique_name', 'unique(name)', 'The name must be unique!')
    ]

    @api.model
    def create(self, vals):
        print("\n[NEW OBJECT CREATE] vals:", vals)
        if vals.get('name'):
            vals['name'] = vals['name'].upper()
            print(f"[NEW OBJECT CREATE] Converted to uppercase: {vals['name']}")
        rec = super().create(vals)
        print(f"[NEW OBJECT CREATE] Created record: {rec.name}")
        return rec

    def name_get(self):
        print(f"[NAME_GET] Called for IDs: {self.ids}")
        return [(record.id, record.name or '') for record in self]

    @api.model
    def name_search(self, name='', args=None, operator='ilike', limit=100):
        print(f"[NAME_SEARCH] Searching for: {name}")
        args = args or []
        if name:
            if isinstance(name, str):
                args += [('name', operator, name.upper())]
            elif isinstance(name, int):
                args += [('id', '=', name)]
        recs = self.search(args, limit=limit)
        print(f"[NAME_SEARCH] Found: {recs.mapped('name')}")
        return recs.name_get()
