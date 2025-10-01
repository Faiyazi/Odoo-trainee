from odoo import models, fields

class AccountAnalyticLine(models.Model):
    _inherit = 'account.analytic.line'

    team_member_id = fields.Many2one('project.team.member', string='Team Member')


    def create(self, vals_list):
        records = super().create(vals_list)
 
        user = records.user_id
        print("\n\n\n\n------user----->", user.name)
        task = records.task_id
        print("\n\n\n\n------task--->",task)
        project = task.project_id if task else False
        print("\n\n\n\n------project--->",project)
        project_team = project.team_id if project else False
        print("\n\n\n\n-------project team----->",project_team)
 
        if user and task and project and project_team:
            #Find a project team member for the user
            team_member = self.env['project.team.member'].search([
                ('user_id', '=', user.id)
            ], limit=1)
            print("\n\n\n\n------team member---->",team_member)
 
 
            #Link the timesheet to the team member
            records.team_member_id = team_member.id
 
            # Add the team to team_member.team_ids if not already present
            if project_team not in team_member.team_id:
                team_member.team_id = [(4, project_team.id)]
 
        return records