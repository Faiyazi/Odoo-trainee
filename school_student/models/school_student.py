from odoo import models, fields, api,_
from odoo.http import request
from odoo.exceptions import ValidationError


class StudentSubject(models.Model):
    _name = 'student.subject'
    _description = 'Student Subject'

    name = fields.Char(string="Subject Name")
    subject_code = fields.Char(string="Subject Code")
    student_marks = fields.Float(string="Student Marks")
    student_id = fields.Many2one('school.student', string="Student name")



class SchoolStudent(models.Model):
    _name = 'school.student'
    _description = 'School Student'
    _rec_name ='student_name'

    teacher_id = fields.Many2one('school.teachers', string="Teacher")
    student_id = fields.Char(string='Student ID:')
    
    status = fields.Selection([('new','New'),('present','Present'),('absent','Absent')],default='new'
                              , group_expand='_read_group_stage_ids')
    student_name = fields.Many2one('res.partner',string='Student Name:' , required=True)
    image_128 = fields.Image(string="Student Image")
    student_email = fields.Char(string='Student Email:')
    dob = fields.Date(string="Birth Date")
    student_phone_no = fields.Char(string='Student Contact no:')
    student_gender = fields.Selection([('male', 'male'), ('female', 'female'), ('other', 'other')], default='male',
                                      required=True)

    parent_name = fields.Char(string="Father or Mother Name")
    parent_phone = fields.Char(string="Contact No")
    street_name = fields.Char(string="Street")
    city = fields.Char(string="City")
    state = fields.Char(string="State")
    student_total_marks = fields.Float(compute='_compute_marks',string='Total marks' ,store=True)
    student_grade = fields.Char(string="Grades")
    class_id = fields.Many2one('student.class', string='Class')
    subject_ids = fields.One2many('student.subject', 'student_id', string='Subjects')

    # For Gantt Chart

    student_starting = fields.Date(string="Starting Day")
    student_ending = fields.Date(string='Ending Day')

    def click_button(self):
        print("You completed an form")
        male_studnet = self.env['school.student'].search([('student_gender', '=', 'male')])
        print('Male Student ==', male_studnet)

        student = self.env.ref("school_student.view_school_student_form")
        print("studentid=", student)

        student_b = self.env["school.student"].browse(1)
        print("student_b=", student_b.id)
        
        
        
        if student_b.exists():
            print('yes its exists')
        
        else:
            student_r = student_b.read(['student_name'])
            print('search_read',student_r)
        #
        # student_s_r = self.env['school.student'].search_read(domain=[('student_marks', '>=', '60')],
        #                                                      fields=['student_name', 'student_marks'])
        # print((student_s_r))

        # vals = {
        #     "name": "From python"
        # }

        # student_c = self.env['student.subject'].create(vals)
        # print("created: ", student_c)

        # student_k = self.env['student.subject'].browse([4, 5, 6])
        # student_k.unlink()
        #     print("not exists")

        # if student_k.exists():
        #     vals = {
        #         "subject_code": "3333"
        #     }
        #     student_u = student_k.write(vals)  # ✅ Call write on the record
        #     print(student_u)  # Will print True if update is successful
        #
        # student_k.copy()
        #
        # result = self.env['school.student'].read_group(
        #     domain=[],
        #     fields=['student_gender', '__count'],
        #     groupby=['student_gender']
        # )
        # print(result)
        #
        # student_name_s = self.env['school.student'].name_search(
        #     name='joy'
        # )
        # print('Name Search', student_name_s)

    def show_rainbow(self):
        return {
            'effect': {
                'fadeout': 'slow',
                'message': 'this is rainbow',
                'imag_url': '/school_student/static/src/img/sc.png',
                'type': 'rainbow_man'

            }
        }
        
    def _read_group_stage_ids(self,stages,domain):
        return [key for key,_ in self._fields['status'].selection]
        

    # @api.model_create_multi
    # def create(self, vals):
    #     existing_student = request.env['school.student'].search([])
    #     print(existing_student)
    #     for student in existing_student:
    #         if student.student_id == vals['student_id']:
    #             raise ValidationError('A student with this id exists.')
    #     return super().create(vals)

    # def write(self, vals):
    #     existing_student = request.env['school.student'].search([])
    #     print(existing_student)
    #     for student in existing_student:
    #         if student.student_id == vals.get('student_id'):
    #             raise ValidationError('A student with this id exists.')
    
    #     return super().write(vals)

    @api.depends('subject_ids.student_marks')
    def _compute_marks(self):
        for rec in self:
            rec.student_total_marks = sum(sub.student_marks for sub in rec.subject_ids)


    @api.onchange('student_name')
    def _onchange_partner_id(self):
        if self.student_name: 
            self.student_phone_no = self.student_name.phone
            self.image_128 = self.student_name.image_1920
            self.student_email = self.student_name.email or self.student_email
        else:
            self.student_phone_no = False
            print('hello')