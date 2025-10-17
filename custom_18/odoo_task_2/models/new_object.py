
from odoo import models, fields, api

class NewObject(models.Model):
    _name = "new.object"
    _description = "New Object with Name Field"

    name = fields.Char(string="Name", required=True)


    def name_search(self, name='', args=None, operator='ilike', limit=100):
        # Convert search input to uppercase for consistent search
        if name:
            name = name.upper()
        return super().name_search(name=name, args=args, operator=operator, limit=limit)


