# -*- coding: utf-8 -*-
##############################################################################
#                                                                            #
# Part of Caret IT Solutions Pvt. Ltd. (Website: www.caretit.com).           #
# See LICENSE file for full copyright and licensing details.                 #
#                                                                            #
##############################################################################

from odoo import models, api
from lxml import etree

class Base(models.AbstractModel):
    _inherit = 'base'

    @api.model
    def get_views(self, views, options=None):
        """
        This method is called whenever Odoo loads a view.
        We will inject 'delete="0"' into the arch dynamically.
        """
        res = super(Base, self).get_views(views, options=options)
        
        for view_type in ['form', 'list']:
            if view_type in res['views']:
                view_data = res['views'][view_type]
                arch = etree.fromstring(view_data['arch'])
                
                arch.set('delete', '0')
                
                view_data['arch'] = etree.tostring(arch, encoding='unicode')
                
                if 'toolbar' in view_data and 'action' in view_data['toolbar']:
                    view_data['toolbar']['action'] = [
                        act for act in view_data['toolbar']['action'] 
                        if act.get('name') != 'Delete'
                    ]
                    
        return res