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
    role = fields.Many2one('school.role',string="Role")
    teacher_name = fields.Char(string="Name")
    teacher_contact = fields.Char(string="Contact No")
    teacher_age = fields.Integer(string="Age")
    teacher_email = fields.Char(string="Email")
    teacher_image = fields.Image(string="Teacher Image")
    teacher_department = fields.Many2many('school.department',string="Department")
    teacher_subject = fields.Many2many('student.subject',string="Subject")
    class_ids = fields.Many2one(
    'student.class', 
    string="Assigned Class",
    domain="[('class_name', '=', False)]"
)
    teacher_gender = fields.Selection([('male','Male'),('female','Female')],string='Gender',required=True,tracking=True,default='male')
    teacher_status = fields.Selection([('present','Present'),('absent','Absent')],string='Status',required=True,tracking=True,default='present')

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            # 1. Handle Sequence Generation
            if vals.get('teacher_id', 'New') == 'New':
                vals['teacher_id'] = self.env['ir.sequence'].next_by_code('school.teacher.id') or 'New'
            
            # 2. Handle Validation (Check if ID already exists)
            # Note: We check the database for the ID inside the loop
            existing_teacher = self.search([('teacher_id', '=', vals.get('teacher_id'))], limit=1)
            if existing_teacher:
                raise ValidationError(_('Teacher ID %s already exists!') % vals.get('teacher_id'))

        # 3. Call super once with the modified list
        return super(SchoolTeacher, self).create(vals_list)


    @api.constrains('teacher_age', 'teacher_subject','class_ids')
    def _check_teacher_rules(self):
        for rec in self:
            if rec.teacher_age < 18:
                raise ValidationError('Age must be more than eighteen (18)')
            
           
            if rec.id:
                existing_record = self.browse(rec.id)
                if existing_record.class_ids and not rec.class_ids:
                    raise ValidationError("Warning: You cannot remove a teacher from an assigned class!")
           
    @api.onchange('class_ids')
    def _onchange_class_ids(self):
        if self.class_ids:
            self.class_ids.class_teacher = self._origin.id or self.id
            
            
class Department(models.Model):
    _name = 'school.department'
    _description = 'Departments'
    _rec_name = 'department_name'
    
    department_name = fields.Char('Department')
    hod = fields.Many2one('school.teachers',string="H.O.D")
    teacher_dep = fields.Many2many('school.teachers',string='Teacher')
    subject_ids = fields.Many2many('student.subject',string='Subject')
    
    