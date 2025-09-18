from odoo import models, fields, api, _
from odoo.exceptions import ValidationError, RedirectWarning

import logging

_logger = logging.getLogger(__name__)

class CollegeStaff(models.Model):
    _name = "college.staff"
    _inherits = {"person.base": "person_id"}
    _description = "College Staff"

    person_id = fields.Many2one('person.base', required=True, ondelete='cascade')
    staff_code = fields.Char(string="Staff Code")
    dob = fields.Date("Date of Birth")
    role = fields.Selection([
        ('lecturer', 'Lecturer'),
        ('admin', 'Admin'),
        ('librarian', 'Librarian'),
        ('other', 'Other')
    ], string="Role")
    joining_date = fields.Datetime(string="Joining Date")


#RedirectWarning exception used this
    def unlink(self):
        for rec in self:
            if not rec.staff_code:
                form_view = self.env.ref("college_erp.college_staff_views_form")
                action = {
                    'type': 'ir.actions.act_window',
                    'res_model': 'college.staff',
                    'res_id': rec.id,
                    'view_mode': 'form',
                    'views': [(form_view.id, 'form')],
                    'target': 'current',
                }
                raise RedirectWarning(
                    _("Staff Code cannot be empty. Before deleting, please fill it in."),
                    action,
                    _("Go to Staff Form")
                )
            return super().unlink()

