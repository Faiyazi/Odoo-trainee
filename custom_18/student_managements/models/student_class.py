from odoo import models, fields


class StudentClass(models.Model):
    _name = 'student.class'
    _description = 'Class Info'

    name = fields.Char(string='Class Name', required=True)
    teacher = fields.Char(string='Class Teacher')