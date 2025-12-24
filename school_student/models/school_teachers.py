from odoo import models, fields, api
from odoo.api import ValuesType, Self
from odoo.exceptions import ValidationError, UserError, RedirectWarning, MissingError
from datetime import datetime, timedelta, date


class SchoolTeacher(models.Model):
    _name = "school.teachers"
    _description = "Teacher"
    _rec_name = 'teacher_name'
    _inherit = ['mail.thread','mail.activity.mixin']
    
    
    teacher_id = fields.Char(string='Teacher ID', copy=False, required=True,
                            default='New')
    user_id = fields.Many2one('res.users', string="Related User")
    teacher_name = fields.Char(string="Name")
    teacher_contact = fields.Char(string="Contact No")
    teacher_age = fields.Integer(string="Age")
    teacher_email = fields.Char(string="Email")
    teacher_image = fields.Image(string="Teacher Image")
    teacher_department = fields.Many2many('school.department',string="Department")
    teacher_subject = fields.Many2many('student.subject',string="Subject")
    class_ids = fields.One2many('student.class', 'class_teacher', string="Assigned Classes")

    @api.model_create_multi
    def create(self, vals):
        existing_ele = self.env['school.teacher'].search([])

        if existing_ele.teacher_id == vals.get('teacher_id'):
            raise ValidationError('its exists')

        return super().create(vals)
    
    def create(self,vals):
        if vals.get('teacher_id','New') == 'New' :
            vals['teacher_id'] = self.env['ir.sequence'].next_by_code('school.teacher.id') or 'New'

        res = super(SchoolTeacher,self).create(vals)
        return res


    @api.constrains('teacher_age', 'teacher_subject')
    def _check_teacher_rules(self):
        for rec in self:
            if rec.teacher_age < 18:
                raise ValidationError('Age must be more than eighteen (18)')
            
            if len(rec.teacher_subject) > 2:
                raise ValidationError('A teacher is only allowed to teach a maximum of two subjects.')


class Department(models.Model):
    _name = 'school.department'
    _description = 'Departments'
    _rec_name = 'department_name'
    
    department_name = fields.Char('Department')
    subject_ids = fields.Many2many('student.subject',string='Subject')