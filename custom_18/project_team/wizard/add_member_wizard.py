from odoo import models, fields, api

class AddMemberWizard(models.TransientModel):
    _name = 'add.member.wizard'
    _description = 'One Member At Time Multiple Team Added Wizard'

    member_id= fields.Many2one('project.team.member',string="Select Member" ,required=True)


    def add_member_team(self):
        teams = self.env['project.team'].browse(self.env.context.get('active_ids', []))
        if not teams:
            return
        for team in teams:
            team.write({
                'team_members':[(4,self.member_id.id)]
            })


