from odoo import models, fields, api 


class ProjectProject(models.Model):
    _inherit = 'project.project'

    team_id = fields.Many2one('project.team', string="Project Team")
    user_ids = fields.Many2many('res.users', string="Project Members")
    

    @api.onchange('team_id')
    def _onchane_team_id(self):
        if self.team_id:
            user_ids = self.team_id.team_member.mapped('user_id')
            self.user_ids = [(6, 0, user_ids)]

    team_member_id = fields.Many2many( related='team_id.team_member', string='Team Members')
    description_1 = fields.Text(string=' Custom Description', index=True)