from odoo import models, fields, api, _
from odoo.exceptions import ValidationError, UserError
from datetime import date

class Student(models.Model):
    _name = 'student.management'
    _description = 'Student Record'
    _rec_name = 'student_code'

    name = fields.Char(string='Name', help='Full name of the student',translate=True)
    student_code = fields.Char(string='Student Code', readonly=True, copy=False, default='New')
    age = fields.Integer(string="Age", compute='_compute_age', readonly=True, store=True)
    gpa = fields.Integer(string="Marks", required=True)
    birth_date = fields.Date(string="Birth Date")
    result = fields.Selection([
        ('pass', 'Pass'),
        ('fail', 'Fail')],
        compute='_compute_result',
        readonly=False,
        string="Result",
        store=True)
    
    address = fields.Text(string="Address")
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other')],
        string="Gender", required=True)



    class_id = fields.Many2one('student.class', string="Class", ondelete='cascade')
    subject_id = fields.Many2many('student.subject', string="Subjects", required=True)

  
    
    @api.model_create_multi
    def create(self, vals_list):
        print("\n\n",vals_list)
        for vals in vals_list:
            if vals.get('student_code', 'New') == 'New':
                vals['student_code'] = self.env['ir.sequence'].next_by_code('student.management') or 'New'
        return super().create(vals_list)

    @api.depends('gpa')
    def _compute_result(self):
        for rec in self:
            if rec.gpa >= 35:
                rec.result = 'pass'
            else:
                rec.result = 'fail'
            
    
    @api.depends('birth_date')
    def _compute_age(self):
        for record in self:
            if record.birth_date:
                today = date.today()
                record.age = today.year - record.birth_date.year - (
                    (today.month, today.day) < (record.birth_date.month, record.birth_date.day)
                )
            else:
                record.age = 0

    @api.constrains('age')
    def _check_age(self):
        for rec in self:
            if rec.age < 5:
                raise UserError("Age should not be less than 5.")

