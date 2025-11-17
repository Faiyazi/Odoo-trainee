from odoo import models, fields

class AddMemberWizard(models.TransientModel):
    _name = 'add.member.wizard'
    _description = "Add Team Memebr to Selected Teams"


    member_id = fields.Many2one('project.team.member', 
                                string="Team Member", 
                                required=True,
                                )
    
    def action_add_member(self):
        print("\n\n\n\n\n\n------------------>",self)
        active_ids = self.env.context.get('active_ids', [])
        if not active_ids:
            return
        
        teams = self.env['project.team'].browse(active_ids)

        for team in teams:
            team.write({
                'team_member': [(4, self.member_id.id)]
            })