from odoo import fields,models,api

class ProjectProject(models.Model):
    _inherit='project.project'

    team_id=fields.Many2one('project.team',string='Team')
    member_ids=fields.Many2many('project.team.member',string='Team Members')

    #Describe usage of index in comment.
    description_1 = fields.Text(string="Description(team)", index=True)

    @api.onchange("team_id")
    def _onchange_team_id(self):
        """Auto-fill members when a team is selected"""
        if self.team_id:
            self.member_ids = [(6, 0, self.team_id.team_members.ids)]
