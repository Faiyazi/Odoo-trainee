from odoo import models, fields

class StudentSearchWizard(models.TransientModel): #transient model
    _name = 'student.search.wizard'
    _description = 'Student Search Wizard'

    course_name = fields.Char(string="Course Name")
    student_ids = fields.Many2many('college.student.admission', string="Students")

    def action_search_students(self):
        students = self.env['college.student.admission'].search([('course', 'ilike', self.course_name)])
        self.student_ids = students.ids