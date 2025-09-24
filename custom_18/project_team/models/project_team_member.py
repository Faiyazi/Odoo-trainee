from odoo import models, fields, api
from odoo.exceptions import UserError  


class ProjectTeamMember(models.Model):
    _name = "project.team.member"
    _description = "Project Team Member"


    name = fields.Char(string="Name", required=True)
    address = fields.Char(string="Address")
    house_no = fields.Char(string="House No")
    street = fields.Char(string="Street")
    street2 = fields.Char(string="Street2")
    country_id = fields.Many2one('res.country', string="Country")
    state_id = fields.Many2one('res.country.state', string="State" ,domain="[('country_id','=',country_id)]")
    city_id = fields.Many2one('res.state.city', string="City",domain="[('state_id','=',state_id)]")
    zip_code = fields.Char(string="Zip Code")
    mobile = fields.Char(string="Mobile")
    user_id = fields.Many2one('res.users', string="User", required=False,
                              context={'search_default_employee': 1})
    email = fields.Char(string="Email", related="user_id.email", store=True)
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    ], string="Gender", default="male")
    dob = fields.Date(string="Date of Birth")
    image = fields.Binary(string="User Image")
    bio_data = fields.Html(string="Bio Data")
    active = fields.Boolean(string="Active", default=True)
    project_id=fields.Many2one('project.project',string='Projects')
    timesheet_ids = fields.One2many('account.analytic.line','project_team_member_id',
                                    string="Timesheets")#project_team_member_id this is many2one create of one2many
    team_id = fields.Many2one("project.team", string="Team",)
    partner_id = fields.Many2one("res.partner", string="Partner")
    task_ids=fields.Many2many("project.task",string="Tasks")
    employee_id = fields.Many2one('hr.employee', string="Employee Id")  # add this


    #it not copy the user(Restrict duplicate user)
    def copy(self , default=None):
        raise UserError("You cannot duplicate the user")

    # #added automatically in the this
    # @api.depends('employee_id', 'project_id')
    # def _compute_timesheets(self):
    #     for member in self:
    #         if member.employee_id and member.project_id:
    #             member.timesheet_ids = self.env['account.analytic.line'].search([
    #                 ('employee_id', '=', member.employee_id.id),
    #                 ('project_id', '=', member.project_id.id)
    #             ])
    #         else:
    #             member.timesheet_ids = False

    #New Add on the project.team.member then new user created
    @api.model
    def create(self, vals):
        if vals.get('user_id'):
            user = self.env['res.users'].browse(vals['user_id'])
            if user and not vals.get('email'):
                vals['email'] = user.email  # auto-fill email from selected user
            return super(ProjectTeamMember, self).create(vals)

        name = vals.get('name')
        email = vals.get('email')

        if not email:
            email = name.replace(" ", "").lower()
            vals['email'] = email

        existing_user = self.env['res.users'].search([('login', '=', email)], limit=1)
        if existing_user:
            vals['user_id']=existing_user.id
        else:
            new_user = self.env['res.users'].create({
                'name': name,
                'login': email,
                'email': email,
            })
            vals['user_id'] = new_user.id
            # 4️⃣ Auto-fill employee_id based on user_id
            if vals.get('user_id') and not vals.get('employee_id'):
                hr_emp = self.env['hr.employee'].search([('user_id', '=', vals['user_id'])], limit=1)
                vals['employee_id'] = hr_emp.id

        member = super(ProjectTeamMember, self).create(vals)
        return member

    #display name/email
    @api.depends('name', 'email')
    def _compute_display_name(self):
        for user in self:
            if user.name:
                user.display_name = f"{user.name}/{user.email}" if user.email else user.name
            else:
                user.display_name = False


