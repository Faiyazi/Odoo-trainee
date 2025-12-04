from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


class ProjectTask(models.Model):
    _inherit = "project.task"
    _order = "name asc"

    assign_date = fields.Datetime("Assigned Date",)
    team_member_ids = fields.Many2many('project.team.member', string="Team Members")


    hide_assign_date = fields.Boolean(
        compute="_compute_hide_assign_date",
        store=False
    )

    # Show only when stage is New or In Progress
    def _compute_hide_assign_date(self):
        for task in self:
            task.hide_assign_date = task.stage_id.name in ["New", "In Progress"]


    # Set assigned_date automatically when task is created
    @api.model
    def create(self, vals):
        if 'assign_date' not in vals:
             vals['assign_date'] = fields.Datetime.now()
        return super(ProjectTask, self).create(vals)

    # Restrict user from assigning a past date manually
    def write(self, vals):
        if 'assign_date' in vals:
            assign_date = fields.Datetime.from_string(vals.get('assign_date'))
            if assign_date < fields.Datetime.now():
                raise ValidationError(_("You cannot set the assigned date to a past date."))
        return super(ProjectTask, self).write(vals)

    # In progress stage task then it not delete raise error
    def unlink(self):
        for task in self:
            try:
                 in_progress_stage = self.env.ref('project.project_stage_1', raise_if_not_found=False)
            except ValueError:
                in_progress_stage = False

            if in_progress_stage and task.stage_id.id == in_progress_stage.id:
                raise ValidationError(_("You cannot delete a task that is in progress."))

        return super(ProjectTask, self).unlink()
