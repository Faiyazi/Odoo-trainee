from odoo import models, fields


class ResPartner(models.Model):
    _inherit = "res.partner"


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
        if self.type2 == "school":
            return "odoo_task_1/static/img/school.png"
        if self.type2 == "individual":
            return "odoo_task_1/static/img/avatar_grey.png"
        if self.type2 == "school_cluster":
            return "odoo_task_1/static/img/school_cluster.jpg"
        if self.type2 == "autarquia":
            return "odoo_task_1/static/img/autarquia.png"
        if self.type2 == "cim":
            return "odoo_task_1/static/img/cim.png"
        if self.type2 == "company":
            return "odoo_task_1/static/img/company_image.png"
        return super()._avatar_get_placeholder_path()