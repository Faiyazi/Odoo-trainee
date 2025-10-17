

from odoo import models, fields, api

class ResPartnerInherit(models.Model):
    _inherit = "res.partner"

    new_object_id = fields.Many2one('new.object', string="New Object")

    @api.model
    def create(self, vals):
        vals = self._normalize_new_object(vals)

        partner_name = vals.get('name')
        if partner_name:
            # Check if partner exists
            existing_partner = self.env['res.partner'].search([('name', '=', partner_name)], limit=1)
            if existing_partner:
                # Update existing partner safely
                existing_partner.write(vals)
                return existing_partner

        # Otherwise, create a new partner
        return super().create(vals)

    def write(self, vals):
        vals = self._normalize_new_object(vals)
        return super().write(vals)

    def _normalize_new_object(self, vals):
        """Handle Many2one from import or manual entry safely."""
        new_obj_val = vals.get('new_object_id')

        # If it's a list (from import), take the first valid element
        if isinstance(new_obj_val, list):
            new_obj_val = next((x for x in new_obj_val if x), None)

        # If it's a string, normalize to uppercase and create/find object
        if isinstance(new_obj_val, str) and new_obj_val.strip():
            new_obj_val = new_obj_val.upper()
            existing_obj = self.env['new.object'].search([('name', '=', new_obj_val)], limit=1)
            if not existing_obj:
                existing_obj = self.env['new.object'].create({'name': new_obj_val})
            vals['new_object_id'] = existing_obj.id
        else:
            # Remove key if invalid to avoid errors
            vals.pop('new_object_id', None)

        return vals

