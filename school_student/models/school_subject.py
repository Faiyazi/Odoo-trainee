from odoo import models, fields, api,_
from odoo.http import request
from odoo.exceptions import ValidationError


class StudentSubject(models.Model):
    _name = 'student.subject'
    _description = 'Student Subject'

    name = fields.Char(string="Subject Name")
    subject_code = fields.Char(string="Subject Code")
    subject_credit = fields.Float(string="Subject Credit")
    department_ids = fields.Many2many('school.department',string='Department')
    student_id = fields.Many2one('school.student', string="Student name",ondelete="cascade")
    
    
    @api.model_create_multi
    def create(self, vals_list):

        for vals in vals_list:
            # Cap credit at 10
            if vals.get('subject_credit', 0) > 10:
                vals['subject_credit'] = 10

            # Optional extra safety check
            if vals.get('subject_code'):
                exists = self.search_count([
                    ('subject_code', '=', vals['subject_code'])
                ])
                if exists:
                    raise ValidationError("This subject code already exists.")

        return super().create(vals_list)


    def write(self, vals):

        # Cap credit at 10
        if vals.get('subject_credit', 0) > 10:
            vals['subject_credit'] = 10

        # Duplicate check excluding current record
        if vals.get('subject_code'):
            exists = self.search_count([
                ('subject_code', '=', vals['subject_code']),
                ('id', '!=', self.id)  # exclude current record
            ])
            if exists:
                raise ValidationError("This subject code already exists.")

        return super().write(vals)