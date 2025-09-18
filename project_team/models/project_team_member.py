from odoo import models, fields, api
from odoo.exceptions import ValidationError


class TeamMember(models.Model):
    _name = 'project.team.member'
    _description = 'Project Team Member'

    user_id = fields.Many2one('res.users', string='User',context="{'search_default_employee': 1}",
                              )
    name = fields.Char(string='Name')
    email = fields.Char(string='Email', related='user_id.email',readonly=False,store=True)
    address = fields.Char(string='Address')
    house_no = fields.Char(string='House No')
    street = fields.Char(string='Street')
    street2 = fields.Char(string='Street2')
    country_id = fields.Many2one('res.country',
                                 string='Country')
    state_id = fields.Many2one('res.country.state', string='State')
    city = fields.Many2one('res.state.city', string='City')
    zip_code = fields.Char(string='Zip Code')
    mobile = fields.Char(string='Mobile No')
    member_ids = fields.Many2many('project.team','team_id',string="Team")
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
        ('others', 'Others')],
        default=''
    )
    dob = fields.Date(string='Birth Day')
    image= fields.Binary(string="Image" ,store=True)
    bio_data = fields.Html(string='Bio data')
    description = fields.Text(string='Description' , index=True)
    # Index help to search and filter the data for database

    timesheet_ids = fields.One2many(
        comodel_name='account.analytic.line',
        inverse_name='time_sheet_id',
        string="Timesheets"
    )

    is_active = fields.Boolean(string='Active', default=True)
    display_name = fields.Char(
        compute='_compute_display_name',
        string='Display Name',
        store=True
    )

    @api.model
    def create(self, vals):

        if not vals.get('user_id') and vals.get('email'):
            new_user = self.env['res.users'].create({
                'name': vals.get('name'),
                'login': vals.get('email'),
                'email': vals.get('email'),
            })
            vals['user_id'] = new_user.id

        # 3. Call super to create Team Member
        res = super(TeamMember, self).create(vals)
        return res

    def copy(self, default=None):
        raise ValidationError("This model can't be copied")

    @api.depends('name', 'user_id','email')
    def _compute_display_name(self):
        for rec in self:
            if rec.user_id:
                rec.display_name = f"{rec.name or ''} / {rec.email or ''}"

            else:
                rec.display_name = self.name or ''

    @api.constrains('mobile')

    def contact(self):
        for rec in self:
            if len(rec.mobile) != 10  :
                raise ValidationError('Its length should be 10')

            if not rec.mobile.isdigit() :
                raise ValidationError('Its should be Number ')

