from odoo import models, fields


class StudentClass(models.Model):
    _name = 'student.class'
    _description = 'Student Class'
    _rec_name = 'class_name'
    _order = 'class_name'

    class_name = fields.Char(string="Class")
    class_total = fields.Integer(string="Total Student")
    student_id=fields.One2many('school.student','class_id',string='Name')
