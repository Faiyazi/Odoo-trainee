from odoo import models, fields, api
from odoo.exceptions import ValidationError
import re


class StudentClass(models.Model):
    _name = 'student.class'
    _description = 'Student Class'
    _rec_name = 'class_name'
    _order = 'class_name'

    class_name = fields.Char(string="Class", required=True)
    section = fields.Char(string="Section")

    class_teacher = fields.Many2one(
        'school.teachers',
        string="Class Teacher",
        domain="[('class_ids','=',False)]"
    )
    
    class_subject = fields.Many2many('student.subject',string='Subject')

    class_rep_b = fields.Many2one('school.student', string="Class Boy's Representative")
    class_rep_g = fields.Many2one('school.student', string="Class Girl's Representative")

    student_id = fields.One2many(
        'school.student',
        'class_id',
        string='Students'
    )

    class_total = fields.Integer(
        string="Total Students",
        compute='_comp_total_strength',
        store=True
    )

    _sql_constraints = [
        ('unique_class_name', 'unique(class_name)', 'This class name already exists!')
    ]

    # ---- COMPUTE TOTAL STUDENTS ----
    @api.depends('student_id')
    def _comp_total_strength(self):
        for rec in self:
            rec.class_total = len(rec.student_id.ids)

    # ---- CLEAN + NORMALIZE CLASS NAME ----
    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if vals.get('class_name'):
                name = vals['class_name'].strip().capitalize()
                name = re.sub(r'([a-zA-Z])(\d)', r'\1 \2', name)
                vals['class_name'] = name

                clean_new = name.replace(' ', '').lower()

                existing = self.search([])
                for record in existing:
                    if record.class_name.replace(' ', '').lower() == clean_new:
                        raise ValidationError(f"The class '{name}' already exists!")

        return super().create(vals_list)

    def write(self, vals):
        if 'class_name' in vals and vals['class_name']:
            name = vals['class_name'].strip().capitalize()
            name = re.sub(r'([a-zA-Z])(\d)', r'\1 \2', name)
            vals['class_name'] = name

        return super().write(vals)

    # ---- ENSURE NORMALIZED UNIQUE NAME ----
    @api.constrains('class_name')
    def _check_unique_normalized(self):
        for rec in self:
            curr_name = re.sub(r'\s+', '', rec.class_name).lower()
            others = self.search([('id', '!=', rec.id)])
            for other in others:
                if other.class_name and re.sub(r'\s+', '', other.class_name).lower() == curr_name:
                    raise ValidationError("A similar class name already exists!")
