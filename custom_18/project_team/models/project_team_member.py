from odoo import models, fields

class ProjectTeamMember(models.Model):
    _name = 'project.team.member'
    _description = 'Project Team Member'
    _rec_name = 'name'

    name = fields.Char(string="Name", help="Enter the full name.", translate=True)
    address = fields.Text(string='Address')
    house_no = fields.Char(string="House No.")
    slistt = fields.Char(string="Slistt")
    slistt2 = fields.Char(string="Slistt2")
    country_id = fields.Many2one('res.country', related='state_id.country_id', string="Country", help="Select country")
    state_id = fields.Many2one('res.country.state', string="State",  help="Select state")
    city_id = fields.Many2one('res.state.city', string="City")
    zip_code = fields.Char(string="ZIP Code", help="Enter postal code")
    mobile = fields.Char(string="Mobile")
    user_id = fields.Many2one('res.users', string="User", domain="[('employee_ids', '!=', False)]")
    email_id = fields.Char(related='user_id.email', string='Email')
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other')],
        string='Gender', required=True)
    birth_date = fields.Date(string='DOB')
    user_image = fields.Binary(string='User Image')
    bio_data = fields.Html(string='Bio Data')
    active = fields.Boolean(string='Active', default=True)
    timesheet_ids = fields.One2many('account.analytic.line', 'team_member_id', string='Timesheet')
    team_id = fields.Many2many('project.team', string="Team")

    

