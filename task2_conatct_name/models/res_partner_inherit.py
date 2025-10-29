from odoo import models, fields, api

class ResPartnerInherit(models.Model):
    _inherit = 'res.partner'

    new_object_id = fields.Many2one('contact.name', string='Object Name')

    @api.model
    def create(self, vals):
        # Check if partner with same name and object already exists
        existing = self.search([
            ('name', '=', vals.get('name')),
            ('new_object_id', '=', vals.get('new_object_id'))
        ], limit=1)

        # Optional: normalize the name before comparison or save
        if vals.get('name'):
            vals['name'] = vals['name'].strip().title()  # e.g. "john doe" → "John Doe"

        if existing:
            # Update existing record instead of creating a new one
            existing.write(vals)
            return existing

        # Otherwise create a new partner
        return super(ResPartnerInherit, self).create(vals)
