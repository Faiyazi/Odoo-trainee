from odoo import models, fields

class Res_Config(models.TransientModel):
    _inherit = "res.config.settings"
    
    message = fields.Char(sting='message', config_parameter="owl_js.message")
    
    effect_type = fields.Selection([
        ('rainbow', 'Rainbow'),
        ('success', 'Success'),
        ('confetti', 'Confetti'),
    ], string="Effect Type", config_parameter="owl_js.effect_type")