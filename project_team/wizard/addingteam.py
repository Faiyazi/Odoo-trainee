from odoo import models, fields


class AddingTeams(models.TransientModel):
    _name = 'add.team'
    _description = 'Adding Team'

    team_name = fields.Char(string='Team Name')
    team_leader = fields.Char(string='Team Leader')

    def action_confirm(self):
        self.env['project.team'].create({
            'name': self.team_name,
            'team_leader': self.team_leader
        })
