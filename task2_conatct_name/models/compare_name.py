from odoo import models, fields, api

class ResPartnerInherit(models.Model):
    _inherit = 'res.partner'

    new_object_id = fields.Many2one('contact.name', string='Object Name')

    @api.model
    def create(self, vals):
        print("Incoming vals:", vals)
        name = vals.get('name')
        new_obj_val = vals.get('new_object_id')

        # Handle text name (from Excel)
        if new_obj_val and isinstance(new_obj_val, str):
            contact = self.env['contact.name'].search([('name', '=', new_obj_val)], limit=1)
            if not contact:
                contact = self.env['contact.name'].create({'name': new_obj_val})
            vals['new_object_id'] = contact.id

        # Only update if both fields exist
        if name and vals.get('new_object_id'):
            existing = self.search([
                ('name', '=', name),
                ('new_object_id', '=', vals['new_object_id'])
            ], limit=1)
            if existing:
                existing.write(vals)
                return existing

        return super(ResPartnerInherit, self).create(vals)
