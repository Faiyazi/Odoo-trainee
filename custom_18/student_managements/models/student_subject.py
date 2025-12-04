from odoo import models, fields


class StudentSubject(models.Model):
    _name = 'student.subject'
    _description = 'Subjects'

    name = fields.Char(string='Subject Name', required=True)
    code = fields.Char(string='Code Name')