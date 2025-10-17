from odoo import models,fields,api

class ContactSelectin(models.Model):
    _inherit='res.partner'
   
    type2 = fields.Selection(
    [('individual', 'Individual'),
     ('school', 'Escola'),
     ('school_cluster', 'Agrupamento'),
     ('autarquia', 'Autarquia'),
     ('cim', 'CIM'),
     ('company', 'Empresa'),
    ], string='Card Type',
    default='',
    relation='company_type'
    )
    
    def _avatar_get_placeholder_path(self):
        if self.is_company:
            return "base/static/img/company_image.png"
        if self.type == 'delivery':
            return "base/static/img/truck.png"
        if self.type == 'invoice':
            return "base/static/img/money.png"
        
        if self.type2 == 'school':
            return "contact_type_selection/static/img/school.png"
        
        if self.type2 == 'school_cluster':
            return "contact_type_selection/static/img/school_cluster.png"
        
        
        if self.type2 == 'autarquia':
            return "contact_type_selection/static/img/autarquia.png"
        
        
        if self.type2 == 'cim':
            return "contact_type_selection/static/img/cim.png"
        
        

            
        return super()._avatar_get_placeholder_path()
  
