from odoo import models, fields, api
from odoo.exceptions import ValidationError



class ProjectTeam(models.Model):
    _name = "project.team"
    _description = "Project Team"
    _order = 'name'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _rec_name="name"


    team_id = fields.Char(string='Team ID', copy=False, readonly=True, required=True, default='New')

    team_member = fields.Many2many('project.team.member', string='Team Member', tracking=True)
    name = fields.Char(string='Team name', required=True,tracking=True )
    team_leader = fields.Many2one('project.team.member', string='Team leader', tracking=True)
    is_active = fields.Boolean(string='Active')
    date = fields.Date.today()


    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if vals.get('team_id', 'New') == 'New':
                team_name = vals.get('name', '')
                seq = self.env['ir.sequence'].next_by_code('project.team') or 'New'
                vals['team_id'] = f"{seq}/{team_name}/{self.date}"

            res = super(ProjectTeam, self).create(vals)

        return res

    def action_open_team_member(self):
        self.ensure_one()
        return {
            'type': 'ir.actions.act_window',
            'name': 'Team Members',
            'res_model': 'project.team.member',
            'view_mode': 'form',
            'domain': [('name', '=', self.team_member)],
            'target': 'current',
        }
        
    @api.constrains("team_leader")
    def _check_team_leader_unique(self):
        for rec in self:
            if rec.team_leader:
                domain = [
                    ("team_leader", "=", rec.team_leader.id),
                    ("id", "!=", rec.id),
                ]
                if self.search_count(domain):
                    raise ValidationError(
                        "This member is already assigned as Team Leader in another team."
                    )