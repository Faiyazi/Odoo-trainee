from odoo import models, fields, api

class StudentResult(models.Model):
    _name = "student.result"
    _description = "Student Result"
    _rec_name = "student_name"

    student_name = fields.Many2one('school.student', string='Student Name', required=True)
    # Related field to automatically fetch class from the student record
    student_class = fields.Many2one('student.class', string="Student Class", 
                                   related='student_name.class_id', store=True)
    result_line_ids = fields.One2many('student.result.line', 'result_id', string="Subject Results")

    @api.onchange('student_name')
    def _onchange_student_name(self):
        """Automatically populate subject lines based on student's class"""
        if self.student_name and self.student_name.class_id:
            lines = []
            # Clear existing lines first
            self.result_line_ids = [(5, 0, 0)]
            # Add subjects linked to the student's class
            for subject in self.student_name.class_id.class_subject:
                lines.append((0, 0, {
                    'student_subject': subject.id
                }))
            self.result_line_ids = lines

class StudentResultLine(models.Model):
    _name = "student.result.line"
    _description = "Student Result Line"
    _rec_name = "student_subject"

    result_id = fields.Many2one('student.result', string="Result Reference", ondelete='cascade')
    student_subject = fields.Many2one('student.subject', string="Subject")
    mid_marks = fields.Float("Mid Term Marks")
    mid_grade = fields.Char("Mid Grade")
    sem_marks = fields.Float('Sem Marks') 
    sem_grade = fields.Char('Sem Grade')
    marks = fields.Float('Total Marks', compute="_compute_total_marks", store=True)
    grade = fields.Char('Total Grade', compute="_compute_total_marks", store=True)

    @api.depends('mid_marks', 'sem_marks')
    def _compute_total_marks(self):
        for line in self:
            line.marks = line.mid_marks + line.sem_marks
            if line.marks >= 80: line.grade = 'A'
            elif line.marks >= 60: line.grade = 'B'
            elif line.marks >= 40: line.grade = 'C'
            else: line.grade = 'F'