from odoo import models, fields, api


class StudentUser(models.Model):
    _name = 'student.user'
    _description = 'Student'

    student_id = fields.Char(string='Student ID')
    name = fields.Char(string='Student Name')
    age = fields.Integer(string='Age')
    course = fields.Selection([('english', 'English'), ('maths', 'Maths'), ('science', 'Science')], default='english',
                              string='Course')
    gender = fields.Selection([('male', 'Male'), ('female', 'Female'), ('other', 'Other')], default='male',
                              string='Gender')

    def create_user_records(self):
        for rec in self:
            query = """
                INSERT INTO student_user (student_id, name, age, course, gender)
                VALUES (%s, %s, %s, %s, %s)
            """
            self.env.cr.execute(query, (rec.student_id, rec.name, rec.age, rec.course, rec.gender))

    def select_user_records(self):
        for rec in self:
            query = """
                SELECT id ,age,student_id from  student_user WHERE course=%s and gender = %s LIMIT 1
            """

            self.env.cr.execute(query, (rec.course, rec.gender))
            result = self.env.cr.fetchone()
            if result:
                return result[0]
            return None

    def update_user_records(self):
        for rec in self:
            query = """
                UPDATE student_user
            SET name=%s, age=%s, course=%s, gender=%s
            WHERE student_id=%s
            """
            self.env.cr.execute(query, (rec.name, rec.age, rec.course, rec.gender, rec.student_id))

    def delete_user_records(self):
        for rec in self:
            query = """
                DELETE FROM student_user WHERE student_id=%s
            """
            self.env.cr.execute(query, (rec.student_id,))
