from odoo import models, fields, api

class AdmissionWizard(models.TransientModel):
    _name = 'admission.wizard'
    _description = 'College Student Admission Wizard'

    student_name = fields.Char(string="Student Name", required=True)
    email = fields.Char(string="Email")
    phone = fields.Char(string="Phone")
    admission_date = fields.Date(string="Admission Date", default=fields.Date.context_today)

    def action_confirm_admission(self):
        """ Apply wizard values to main model """
        active_id = self.env.context.get('active_id')   # get current record
        admission = self.env['college.student.admission'].browse(active_id)
        admission.write({
            'student_name': self.student_name,
            'email': self.email,
            'phone': self.phone,
            'admission_datetime': self.admission_date,
            'state': 'done',   # example: move to confirmed state
        })
        return {'type': 'ir.actions.act_window_close'}  # close wizard
