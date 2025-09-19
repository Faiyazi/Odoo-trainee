import re
import io
import base64
import xlsxwriter
from odoo.http import content_disposition
from odoo.tools.misc import xlsxwriter as odoo_xlsxwriter
from odoo import http
from odoo.http import request
from odoo import models, fields, api, _
from odoo.exceptions import ValidationError, UserError


class CollegeTeacher(models.Model):
    _name = "college.teacher"
    _inherit = "person.base"
    _description = "College Teacher"

    employee_id = fields.Char(string="Employee ID")
    department = fields.Selection([('science', 'Science'), ('commerce', 'Commerce'),
                                   ('arts', 'Arts'), ], string="Department", required=True)
    base_salary = fields.Float(string="Base Salary")
    final_salary = fields.Float(string="Final Salary", compute="_compute_final_salary")
    subject = fields.Char(string="Subject")  # new field specific to teacher(used classical inheritance)
    age = fields.Integer(string="Age")
    # excel report used
    export_file = fields.Binary("Export File", readonly=True)
    export_file_name = fields.Char("File Name", readonly=True)
    # 1. SQL Constraint - employee_id must be unique
    _sql_constraints = [
        ('employee_id_unique', 'unique(employee_id)', 'Employee ID must be unique!'),
    ]

    # 2. Python Constraint - it field added only 10 digit
    @api.constrains('phone')  # @api.constraints decorator used in this code
    def _check_phone_number(self):
        for record in self:
            if record.phone:
                # Check if it has exactly 10 digits
                if not re.fullmatch(r'\d{10}', record.phone):
                    raise ValidationError("Phone number must be exactly 10 digits.")

    # 3. Python Constraint - age must be at least 21
    @api.constrains('age')
    def _check_age(self):
        for teacher in self:
            if teacher.age and teacher.age < 21:
                raise ValidationError("Teacher's age must be at least 21.")

    # @api.depends_context decorator used in this code
    @api.depends('department')
    @api.depends_context('department')
    def _compute_final_salary(self):
        for rec in self:
            dept = self.env.context.get('department')
            if dept == 'commerce':
                rec.final_salary = rec.base_salary * 1.2
            elif dept == 'science':
                rec.final_salary = rec.base_salary * 1.5
            else:
                rec.final_salary = rec.base_salary

    # @api.returns decorator used in this code
    @api.model
    @api.returns('self', lambda value: value.id)
    def get_first_student_for_teacher(self):
        """
        Returns the ID of the first student for API/RPC calls.
        The teacher can use this to fetch student details.
        """
        student = self.env['college.student.admission'].search([], limit=1)
        return student

    # Dynamic fetching method
    @api.model
    @api.returns('self', lambda value: [rec.id for rec in value])
    def get_all_students(self):
        """Return IDs of all students"""
        students = self.env['college.student.admission'].search([])
        return students

    # added the UserError if employee_id is not given then raise this

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if not vals.get('employee_id'):
                raise UserError(_("You must provide an Employee ID for the teacher."))
            # Call the super method to actually create the records
            records = super(CollegeTeacher, self).create(vals_list)
            return records

    def write(self, vals):
        if 'employee_id' in vals and not vals.get('employee_id'):
            raise UserError(_("Employee ID cannot be empty when updating record."))
        return super(CollegeTeacher, self).write(vals)

    def action_export_excel(self):
        """Export teacher data into Excel"""
        self.ensure_one()

        # Create in-memory Excel
        output = io.BytesIO()
        workbook = xlsxwriter.Workbook(output, {'in_memory': True})
        sheet = workbook.add_worksheet("Teacher")

        # Headers
        headers = ["Employee ID", "Employee Name", "Email", "Phone", "Salary"]
        for col, header in enumerate(headers):
            sheet.write(0, col, header)

        # Data row
        sheet.write(1, 0, self.employee_id or '')
        sheet.write(1, 1, self.name or '')
        sheet.write(1, 2, self.email or '')
        sheet.write(1, 3, self.phone or '')
        sheet.write(1, 4, self.final_salary or '')

        workbook.close()
        output.seek(0)

        # Save file into binary field
        file_data = base64.b64encode(output.read())
        self.write({
            'export_file': file_data,
            'export_file_name': 'TeacherReport.xlsx'
        })

        # Return action to download the file
        return {
            'type': 'ir.actions.act_url',
            'url': f"/web/content/{self._name}/{self.id}/export_file/{self.export_file_name}?download=true",
            'target': 'self',
        }
