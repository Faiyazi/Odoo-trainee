from odoo import models, fields, api


class ContactName(models.Model):
    _name = 'contact.name'
    _description = 'Contact Name'

    _sql_constraints = [
        ('unique_name', 'unique(name)', 'Name must be unique!')
    ]

    name = fields.Char(string='Name', required=True)

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if 'name' in vals and vals['name']:
                vals['name'] = vals['name'].upper()
        return super(ContactName, self).create(vals_list)

    def write(self, vals):
        if 'name' in vals and vals['name']:
            vals['name'] = vals['name'].upper()
        return super(ContactName, self).write(vals)
    
    def name_get(self):
        result = []
        for record in self:
            result.append((record.id, record.name))
        return result

    @api.model
    def name_search(self, name='', args=None, operator='ilike', limit=100):
        args = args or []
        if name:
            records = self.search([('name', operator, name)] + args, limit=limit)
        else:
            records = self.search(args, limit=limit)

        if records:
            return records.name_get()
        return super(ContactName, self).name_search(name=name, args=args, operator=operator, limit=limit)

