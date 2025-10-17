from odoo import models,fields,api
from odoo.http import request



class ResPartnerInherit(models.Model):
    _inherit = 'res.partner'

    new_object_id = fields.Many2one('contact.name', string='Object Name')

    @api.model
    def create(self, vals):
        existing = self.search([
            ('name', '=', vals.get('name')),
            ('new_object_id', '=', vals.get('new_object_id'))
        ], limit=1)

        if existing:
            existing.write(vals)
            return existing
        return super(ResPartnerInherit, self).create(vals)

