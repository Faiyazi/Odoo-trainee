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










