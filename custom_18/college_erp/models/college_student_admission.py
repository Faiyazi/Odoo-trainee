from odoo import fields, models, api, _
from odoo.exceptions import ValidationError, AccessError, RedirectWarning
from datetime import date, timedelta
import logging


_logger = logging.getLogger(__name__)


class CollegeStudentAdmission(models.Model):
    _name = "college.student.admission"
    _description = "College Student Admission Form"
    _rec_name = "student_name"


    name = fields.Char(
        string="Admission Number",
        required=True,
        copy=False,
        readonly=True,
        index=True,
        default=lambda self: _('New'))
    user_id = fields.Many2one('res.users', string='Related User')  # links student to Odoo user
    student_name = fields.Char(string="Full Name", copy=False, help="Enter the full name of the student.")
    email = fields.Char(string="Email")
    phone = fields.Char(string="Phone Number")
    dob = fields.Date(string="Date of birth")
    age = fields.Integer(string="Age", compute="_compute_age", readonly=True)
    height = fields.Float(string="Height")
    admission_datetime = fields.Datetime(string="Admission Date & Time", index=True)
    active = fields.Boolean(string="Is Active?", default=True)
    photo = fields.Image(string="Student Photo")
    documents = fields.Binary(string="Upload Document")
    description = fields.Html(string="Description/Notes", translate=True)
    fees_paid = fields.Monetary(string="Fees Paid", currency_field='currency_id')
    currency_id = fields.Many2one('res.currency', string="Currency")
    state = fields.Selection([
        ('draft', 'Draft'),
        ('done', 'Done')
    ], default='draft', string="Status")

    category = fields.Selection([('minor', 'Minor'), ('adult', 'Adult')])

    _sql_constraints = [
        ('email_unique', 'unique(email)', 'The email must be unique!'),
    ]




    #added the object through open the wizard
    def action_open_admission_wizard(self):
        return {
            'type': 'ir.actions.act_window',
            'res_model': 'admission.wizard',
            'view_mode': 'form',
            'target': 'new',
            'context': {'default_student_id': self.id},
        }


    # @api.onchange decorator used in this code
    @api.onchange('age')
    def _onchange_age(self):
        """Automatically update category based on age"""
        if self.age:
            if self.age < 18:
                self.category = 'minor'
            else:
                self.category = 'adult'

    # @api.depends decorator used in this code
    @api.depends('dob')
    def _compute_age(self):
        for rec in self:
            if rec.dob:
                today = date.today()
                dob = rec.dob if isinstance(rec.dob, date) else fields.Date.from_string(rec.dob)
                rec.age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
            else:
                rec.age = 0

    # ---------------- ORM METHODS ----------------
    @api.model_create_multi  # @api.model_create_multi decorator used in this code
    def create(self, vals_list):
        for vals in vals_list:
            # Sequence logic
            #added the sequence on the admission no(student_sequence.xml)
            if vals.get('name', 'New') == 'New':
                vals['name'] = self.env['ir.sequence'].next_by_code('college.student.admission') or 'New'

            # Validation logic
            if not vals.get("student_name"):
                raise ValidationError("Student Name is required!")
            if not vals.get("email"):
                raise ValidationError("Email is required!")
            if not vals.get("phone"):
                raise ValidationError("Phone is required!")

        records = super(CollegeStudentAdmission, self).create(vals_list)
        return records


    @api.model  # @api.model decorator used in this code
    def write(self, vals):
        print(">> My custom write method is called!")  # Debug
        # Check for required fields if updating
        if 'student_name' in vals and not vals.get('student_name'):
            raise ValidationError("Student Name cannot be empty!")
        if 'email' in vals and not vals.get('email'):
            raise ValidationError("Email cannot be empty!")
        if 'phone' in vals and not vals.get('phone'):
            raise ValidationError("Phone cannot be empty!")

        # Call super to actually update the record
        result = super(CollegeStudentAdmission, self).write(vals)
        return result

    @api.model
    def read_group(self, domain, fields, groupby, offset=0, limit=None, orderby=False, lazy=True):
        # call super to get normal grouped data
        res = super().read_group(domain, fields, groupby, offset=0, limit=None, orderby=False, lazy=True)

        # Example: Add a fake field "total_fee" into each group
        for line in res:
            line['fees_paid'] = 50000  # static or computed custom logic
        return res

    @api.model
    def name_search(self, name='', args=None, operator='ilike', limit=100):
        args = args or []
        domain = []
        if name:  # only add search domain if a search term is passed
            domain = [('student_name', operator, name)]
        records = self.search(domain + args, limit=limit)
        return records.name_get()

    @api.model
    def name_get(self):
        res = []
        for record in self:
            display_name = f"{record.student_name}"
            res.append((record.id, display_name))
        return res

    @api.model
    def default_get(self, fields_list):
        res = super().default_get(fields_list)
        if 'admission_date' in fields_list:
            res['admission_date'] = date.today()
        return res

    @api.model
    def check_access(self, mode):
        if mode == 'unlink' and any(record.state == 'done' for record in self):
            raise AccessError("You cannot delete a confirmed admission.")
        return super().check_access(mode)

    def unlink(self):
        for rec in self:
            if not rec.fees_paid:
                # Get the payment form view reference
                form_view = self.env.ref("college_erp.college_student_admission_views_form")    # replace with your
                # view XML ID
                # Prepare the action to redirect
                action = {
                    'type': 'ir.actions.act_window',
                    'res_model': 'college.student.admission',  # replace with your payment model
                    'res_id': rec.id,                        # optional: record ID, or remove if not needed
                    'view_mode': 'form',
                    'views': [(form_view.id, 'form')],
                    'target': 'current',
                }
                # Raise RedirectWarning
                raise RedirectWarning(
                    _("Fees are pending for this student! Before deleting, please complete the payment."),
                    action,
                    _("Go to Payment Page")
                )
        # If fees are paid, allow deletion
        return super(CollegeStudentAdmission, self).unlink()

#added cron through birthday
    @api.model
    def cron_birthday_reminder(self):
        """Cron job: Send personalized birthday reminder 24 hours before birthday"""
        tomorrow = date.today() + timedelta(days=1)

        # Search student whose birthday is tomorrow
        birthday_stud = self.search([
            ("dob", "!=", False),
            ("dob", "like", f"%-{tomorrow.month:02d}-{tomorrow.day:02d}")
        ])

        if not birthday_stud:
            _logger.info("No Student birthday tomorrow.")
            return

        for student in birthday_stud:
            if not student.email:
                _logger.warning("Student %s has no email!", student.name)
                continue

            # Personalized message
            message = f"""
            Hi {student.student_name},<br><br>
            This is a reminder that your birthday is tomorrow! 🎉<br><br>
            Have a wonderful day ahead!<br>
            Best wishes,<br>
            College HR
            """

            # Send email only to this student
            self.env["mail.mail"].create({
                "subject": "Happy Birthday in Advance! 🎂",
                "body_html": message,
                "email_to": student.email,
            }).send()
            _logger.info("Birthday reminder sent to %s <%s>", student.name, student.email)

    def action_done(self):
        for rec in self:
            rec.state='done'

#url action method
    def action_open_website(self):
        return {
            'type': 'ir.actions.act_url',
            'target': 'new',   # "new" opens in new tab, "self" in same window
            'url': 'https://www.odoo.com',
        }
#Client action
    def client_action(self):
         return {
        'type': 'ir.actions.client',
        'tag': 'display_notification',
        'params': {
            'title': 'SuccessFully!',
            'message': 'The Client Action was executed.',
            'sticky': False,
        }
    }
    #send Mail button method
    def action_send_mail(self):
        template = self.env.ref('college_erp.email_template_student_admission')
        template.send_mail(self.id, force_send=True)

