from odoo import models, fields


class ContactsInherit(models.Model):
    _inherit = 'res.partner'

    type2 = fields.Selection(
        [('individual', 'Individual'),
         ('school', 'Escola'),
         ('school_cluster', 'Agrupamento'),
         ('autarquia', 'Autarquia'),
         ('cim', 'CIM'),
         ('company', 'Empresa'),
         ], string='Card Type',
        default='')

    def _avatar_get_placeholder_path(self):
        if self.type2 == 'individual':
            return "contacts_field/static/img/avatar_grey.png"
        if self.type2 == 'school':
            return "contacts_field/static/img/school.png"
        if self.type2 == 'school_cluster':
            return "contacts_field/static/img/school_cluster.png"
        if self.type2 == 'autarquia':
            return "contacts_field/static/img/autarquia.png"
        if self.type2 == 'cim':
            return "contacts_field/static/img/cim.png"
        if self.type2 == 'company':
            return "contacts_field/static/img/company_image.png"
        return super()._avatar_get_placeholder_path()
