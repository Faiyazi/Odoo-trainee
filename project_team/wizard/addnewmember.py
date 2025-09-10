from odoo import models, fields, api


class ProjectTeamWizard(models.TransientModel):
    _name = "project.team.wizard"
    _description = "Project Team Wizard"

    team_member = fields.Many2one(
        "project.team.member",
        string="Team Member",
        required=True,
        ondelete="cascade"
    )

    def action_confirm(self):
        active_ids = self.env.context.get("active_ids", [])
        if active_ids and self.team_member:
            teams = self.env["project.team"].browse(active_ids)
            for team in teams:
                team.write({
                    "team_member": [(4, self.team_member.id)],
                })
