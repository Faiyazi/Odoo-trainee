from odoo import models, fields, api

class ResPartnerInherit(models.Model):
    _inherit = "res.partner"

    new_object_id = fields.Many2one('new.object', string="New Object")

    @api.model
    def load(self, fields_list, data_list):
        print("\n [LOAD] === CUSTOM load() CALLED ===")

        if 'new_object_id' in fields_list:
            idx = fields_list.index('new_object_id')
            print(f"[LOAD] Found 'new_object_id' column at index {idx}")

            for row in data_list:
                val = row[idx]
                print(f"\n[LOAD] Processing row value: {val} ({type(val)})")

                # Skip empty or numeric IDs
                if not val or isinstance(val, int):
                    print("[LOAD] Skipped (empty or ID)")
                    continue

                if isinstance(val, str):
                    name_upper = val.strip().upper()
                    print(f"[LOAD] Checking for existing New Object: '{name_upper}'")

                    obj = self.env['new.object'].search([('name', '=', name_upper)], limit=1)
                    if not obj:
                        obj = self.env['new.object'].create({'name': name_upper})
                        print(f"[LOAD] Created New Object: {obj.name}")
                    else:
                        print(f"[LOAD] Found Existing New Object: {obj.name}")

                    # Replace text with record ID
                    row[idx] = obj.id

        return super().load(fields_list, data_list)

    @api.model
    def create(self, vals):
        print("\n [CREATE] === CREATE CALLED ===")
        print(f"[CREATE] Incoming vals: {vals}")

        # Handle new_object_id (string)
        if vals.get('new_object_id') and isinstance(vals['new_object_id'], str):
            name = vals['new_object_id'].strip().upper()
            print(f"[CREATE] Processing New Object: {name}")
            obj = self.env['new.object'].search([('name', '=', name)], limit=1)
            if not obj:
                obj = self.env['new.object'].create({'name': name})
                print(f"[CREATE] Created new New Object: {obj.name}")
            else:
                print(f"[CREATE] Found existing New Object: {obj.name}")
            vals['new_object_id'] = obj.id

        # Check existing partner
        if vals.get('name'):
            name = vals['name'].strip()
            existing_partner = self.env['res.partner'].search([('name', '=', name)], limit=1)
            if existing_partner:
                print(f"[CREATE] Partner '{name}' already exists.")
                if vals.get('new_object_id'):
                    existing_partner.write({'new_object_id': vals['new_object_id']})
                    print(f"[CREATE] Updated New Object for existing partner: {existing_partner.name}")
                return existing_partner
        return super().create(vals)

    def write(self, vals):
        print("\n [WRITE] === WRITE CALLED ===")
        print(f"[WRITE] Incoming vals: {vals}")

        if 'new_object_id' in vals and isinstance(vals['new_object_id'], str):
            name = vals['new_object_id'].strip().upper()
            print(f"[WRITE] Processing New Object: {name}")
            obj = self.env['new.object'].search([('name', '=', name)], limit=1)
            if not obj:
                obj = self.env['new.object'].create({'name': name})
                print(f"[WRITE] Created new New Object: {obj.name}")
            else:
                print(f"[WRITE] Found existing New Object: {obj.name}")
            vals['new_object_id'] = obj.id

        result = super().write(vals)
        return result

