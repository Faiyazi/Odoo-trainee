# -- coding: utf-8 --
##############################################################################
#                                                                            #
# Part of Caret IT Solutions Pvt. Ltd. (Website: www.caretit.com).           #
# See LICENSE file for full copyright and licensing details.                 #
#                                                                            #
##############################################################################

from odoo import api, models, tools

class IrModelAccess(models.Model):
    _inherit = 'ir.model.access'

    @api.model
    @tools.ormcache('self._uid', 'model', 'mode', 'raise_exception', 'self.env.context.get("lang")')
    def check(self, model, mode='read', raise_exception=True):
        """ Checks if the user has permission to perform the specified operation on a model, 
        restricting deletions based on certain conditions and user group access. """
        result = super().check(model, mode, raise_exception)
        if mode != 'unlink':
            return result
        if self.env.user.has_group('cit_delete_option_config.delete_option_access'):
            return result
        active_model = self.env.context.get('active_model')        
        if model == active_model:
            return False
        if active_model and model != active_model:
            return result   
        
        ModelClass = self.env.get(model)
        if ModelClass is None:
            return result

        is_o2m_line = any(
            f.type == 'many2one' and f.ondelete == 'cascade'
            for f in ModelClass._fields.values()
        )

        if is_o2m_line:
            return True
        
        if model.endswith(('.line', 'stock.move','.item','.detail','.lines')):
            return result
        return False