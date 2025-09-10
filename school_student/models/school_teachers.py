from odoo import models, fields, api
from odoo.api import ValuesType, Self
from odoo.exceptions import ValidationError, UserError, RedirectWarning, MissingError
from datetime import datetime, timedelta, date


class SchoolTeacher(models.Model):
    _name = "school.teachers"
    _description = "School Teacher"

    reference = fields.Char(string='Reference', copy=False, required=True,
                            default='New')
    user_id = fields.Many2one('res.users', string="Related User")
    teacher_name = fields.Char(string="Name")
    teacher_id = fields.Char(string="Teacher ID")
    teacher_contact = fields.Char(string="Contact No")
    teacher_age = fields.Integer(string="Age")
    teacher_email = fields.Char(string="Email")
    teacher_image = fields.Image(string="Teacher Image")
    teacher_department = fields.Char(string="Department")

    @api.model_create_multi
    def create(self, vals):
        existing_ele = self.env['school.teacher'].search([])

        # for stu in existing_ele:
        if existing_ele.teacher_id == vals.get('teacher_id'):
            raise ValidationError('its exists')

        return super().create(vals)
    
    def create(self,vals):
        if vals.get('reference','New') == 'New' :
            vals['reference'] = self.env['ir.sequence'].next_by_code('school.student.id') or 'New'

        res = super(SchoolTeacher,self).create(vals)
        return res


    @api.constrains('teacher_age')
    def constrains_age(self):
        for rec in self:
            if rec.teacher_age < 0:
                raise ValidationError('Age must be more than zero(0)')

            # if rec.teacher_age <18:
            #     raise UserError('You are too young for an teacher ')

            # if rec.teacher_age > 18:
            #     action_id = self.env.ref('school_teacher.action_school_teacher').id
            #     raise RedirectWarning("you are valid but not today", action_id, 'Go to age')

            if not rec.teacher_age:
                raise MissingError('not exists')
