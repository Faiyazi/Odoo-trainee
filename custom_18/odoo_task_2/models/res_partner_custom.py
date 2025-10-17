from odoo import api, fields, models


class PartnerCategoryCustom(models.Model):
    _name = "partner.category.custom"
    _description = "Partner Category Custom"

    name = fields.Char(string="Name", required=True)

    @api.model
    def create(self, vals):
        if vals.get("name"):
            vals["name"] = vals["name"].upper()
        return super().create(vals)

    def name_get(self):
        result = []
        for record in self:
            result.append((record.id, record.name))
        return result

    @api.model
    def name_search(self, name='', args=None, operator='ilike', limit=100):
        args = args or []
        if name:
            args += [('name', operator, name.upper())]
        return self.search(args, limit=limit).name_get()


class ResPartner(models.Model):
    _inherit = 'res.partner'

    custom_category_id = fields.Many2one(
        'partner.category.custom',
        string="Custom Category"
    )
