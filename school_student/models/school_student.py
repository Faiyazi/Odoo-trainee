from odoo import models, fields, api,_
from odoo.http import request
from odoo.exceptions import ValidationError

class SchoolStudent(models.Model):
    _name = 'school.student'
    _description = 'School Student'
    _rec_name ='student_name'
    _inherit = ['mail.thread','mail.activity.mixin']
    

    teacher_id = fields.Many2one('school.teachers', string="Teacher",tracking=True)
    student_id = fields.Char(string='Student ID',default='New',tracking=True)
    
    status = fields.Selection([('present','Present'),('absent','Absent')],default=''
                              , group_expand='_read_group_stage_ids',tracking=True)
    student_name = fields.Many2one('res.partner',string='Student Name:' , required=True,tracking=True)
    image_128 = fields.Image(string="Student Image")
    student_email = fields.Char(string='Student Email:',tracking=True)
    dob = fields.Date(string="Birth Date")
    student_phone_no = fields.Char(string='Student Contact no:',tracking=True)
    student_gender = fields.Selection([('male', 'Male'), ('female', 'Female')], default='',
                                      required=True,tracking=True)
    
    # Parents Details
    parent_name = fields.Char(string="Parent Name",tracking=True)
    parent_phone = fields.Char(string="Contact No")
    parent_email = fields.Char(string="Email")
    parent_dob = fields.Date(string="Birth Day")
    
    
    # Address
    street_name = fields.Char(string="Street")
    city = fields.Char(string="City")
    country = fields.Many2one("res.country", string="Country")
    state = fields.Many2one("res.country.state", string="State")
    
    
    
    student_grade = fields.Char(string="Grades")
    class_id = fields.Many2one('student.class', string='Class',ondelete='set null')
    subject_ids = fields.Many2many('student.subject', 'student_id', string='Subjects')

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

   

    @api.onchange('student_name','class_id')
    def _onchange_partner_id(self):
        if self.student_name: 
            self.student_phone_no = self.student_name.phone
            self.image_128 = self.student_name.image_1920
            self.student_email = self.student_name.email or self.student_email
        else:
            self.student_phone_no = False
            print('hello')
            
        if self.class_id:
            self.subject_ids = self.class_id.class_subject    
            
            
    @api.model_create_multi
    def create(self, vals_list):
        # 1. Prepare vals (Sequence & Validation) BEFORE creating records
        for vals in vals_list:
            if vals.get('student_id', 'New') == 'New':
                vals['student_id'] = self.env['ir.sequence'].next_by_code('school.student.id') or 'New'
            
            # Check if ID exists in DB
            existing = self.search([('student_id', '=', vals.get('student_id'))], limit=1)
            if existing:
                raise ValidationError('Student ID %s already exists!' % vals.get('student_id'))

        # 2. Create the records in the database
        records = super(SchoolStudent, self).create(vals_list)

        # 3. Trigger email logic AFTER records exist in the database
        for record in records:
            if record.status == 'absent':
                record._send_absence_email()

        # 4. Return the created records
        return records
    
    
    def write(self, vals):
        res = super().write(vals)

        if 'class_id' in vals:
            for rec in self:
                cls = rec.class_id
                reps = cls and [cls.class_rep_b.id, cls.class_rep_g.id]
                if rec.id in reps:
                    if rec.id == cls.class_rep_b.id:
                        cls.class_rep_b = False
                    if rec.id == cls.class_rep_g.id:
                        cls.class_rep_g = False
                        
        if 'status' in vals and vals.get('status') == 'absent':
            self._send_absence_email()
                            
        return res
    
    
    
    def _send_absence_email(self):
        # Find your actual template ID (e.g., 'school_student.mail_template_student_absence')
        template = self.env.ref('school_student.template_school_student', raise_if_not_found=False)
        
        if not template:
            return
            
        for record in self:
            # Check if an email exists either on the student record or the linked partner
            email_exists = record.student_email or record.student_name.email
            
            if email_exists:
                # send_mail() uses the template design
                # email_layout_xmlid adds the standard Odoo email wrapper/footer
                template.send_mail(
                    record.id, 
                    force_send=True, 
                    email_values={'email_to': record.student_email or record.student_name.email}
                )
                
                # Optional: Log a simple note in the chatter that the mail was sent
                record.message_post(body=_("Absence notification email sent to %s") % record.student_name.name)