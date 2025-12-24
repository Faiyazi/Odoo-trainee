from odoo import models, fields,api


class StudentClass(models.Model):
    _name = 'student.class'
    _description = 'Student Class'
    _rec_name = 'class_name'
    _order = 'class_name'
    

    class_name = fields.Char(string="Class",required=True)
    section = fields.Char(String="Section")
    class_teacher = fields.Many2one('school.teachers',string="Class Teacher")
    class_rep_b = fields.Many2one('school.student',string="Class Boy's Representive")
    class_rep_g = fields.Many2one('school.student',string="Class Girl's Representive")
    
    class_total = fields.Integer(string="Total Student")
    student_id=fields.One2many('school.student','class_id',string='Students')
    
   