<<<<<<< HEAD
from odoo import models, fields, api
from datetime import date

class ProjectTeam(models.Model):
    _name = "project.team"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Project Team"
    _order = 'name'

    team_members = fields.Many2many('project.team.member',string='Team Members')
    name=fields.Char(string='Name',tracking=True)
    team_leader=fields.Char(string='Team Leader',tracking=True)
    active=fields.Boolean(string='Active',default=True)
    sequence=fields.Char(string='Sequence',readonly=True,copy=False,)
    member_count=fields.Integer(string='Member Count', compute='compute_member_count')
    member_ids = fields.Many2many("project.team.member", "team_id", string="Members")

     #add sequence for this method
    @api.model
    def create(self, vals):
        team = super(ProjectTeam, self).create(vals)
        seq_number = self.env['ir.sequence'].next_by_code('project_team')
        today_date = date.today().strftime('%Y%m%d')
        team_name = team.name or 'NoName'
        team.sequence= f"{seq_number}/{team_name}/{today_date}"
        return team

    #click on the button then open project.team.member
    def action_open_team_members(self):
         return {
            'name':'Team Members',
            'type': 'ir.actions.act_window',
            'res_model': 'project.team.member',
            'view_mode': 'list',
            'domain': [('id', 'in', self.team_members.ids)],
            'context': {'create':False},
            'target': 'current',
        }

    #count the member of all the in the project.team linked with project.team.member
    @api.depends('member_ids')
    def compute_member_count(self):
        for team in self:
            team.member_count = len(team.team_members)









=======
from odoo import models, fields, api, _
from datetime import date

class ProjectTeam(models.Model):
    _name = 'project.team'
    _description = 'Project Team'
    _order = 'name'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name= fields.Char(string='Team Name', required=True, tracking=True, translate=True)
    team_member = fields.Many2many('project.team.member', string='Team Members', tracking=True)
    team_leader = fields.Many2one('res.users', string='Team Leader', tracking=True)
    active = fields.Boolean(string='Active', default=True)
    sequence = fields.Char(string='Team Code', readonly=True, copy=False, default='New')
    user_image = fields.Binary(string='User Image')

    member_count = fields.Integer(string="Member Count", compute="_compute_member_count")

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if vals.get('sequence', _('New')) == _('New'):
                seq = self.env['ir.sequence'].next_by_code('project.team') or 'New'
                team_name = vals.get("name").replace(" ","")
                time = date.today().strftime('%d-%m-%Y')
                vals["sequence"] = f"{seq}/{team_name}/{time}"
        return super().create(vals_list)
    
    @api.depends('member_count')
    def _compute_member_count(self):
        for rec in self:
            rec.member_count = self.env['project.team.member'].search_count([('team_id', '=', rec.id)])


    def action_project_team_member(self):
        return {
            'type': 'ir.actions.act_window',
            'name': 'Team Member',
            'res_model' : 'project.team.member',
            'view_mode': 'list,form',
            'domain': [('team_id', '=', self.id)],
            'target': 'current',
        }

>>>>>>> ronak

