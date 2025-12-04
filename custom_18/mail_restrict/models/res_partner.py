<<<<<<< HEAD
from odoo import fields, models
=======
from odoo import models, fields

>>>>>>> ronak

class ResPartner(models.Model):
    _inherit = 'res.partner'

<<<<<<< HEAD
    restrict_mail = fields.Boolean(string="Restrict mail")

=======
    restrict_mail = fields.Boolean(string='Restrict Mail')
>>>>>>> ronak
