from odoo import models, fields, api
from odoo.exceptions import ValidationError

class ProjectTask(models.Model):
    _inherit = 'project.task'


    progress_percentage = fields.Integer()

    @api.constrains('progress_percentage')
    def _check_percentage_range(self):
        for rec in self:
            if rec.progress_percentage < 0 or rec.progress_percentage > 100:
                raise ValidationError ("Percentage must be between 0 to 100.")
            
    @api.constrains('progress_percentage', 'stage_id')
    def _check_progress_stage(self):
        print("\n\n\n\n\n----------self",self)

        # First Method
        # for task in self:
        #     if task.progress_percentage == 100 and task.stage_id and task.stage_id.name != "Done":
                
        #         done_stage = self.env["project.task.type"].search(
        #             [("name", "=", "Done"),
        #              ("project_ids", "in", [task.project_id.id])
        #              ], limit=1
        #         )
        #         print("\n\n\n\n--------->0000000",done_stage)
        #         print("\n\n\n\n--------->111111",task.stage_id)
        #         if done_stage:
        #             task.stage_id = done_stage.id

        #     if task.stage_id and task.stage_id.name == "Done" and task.progress_percentage < 100:
        #         raise ValidationError("Task in 'Done' stage must have 100% progress.")


        # Second Method
        # for task in self:
                
        #     done_stage = self.env.ref("project.project_stage_2", raise_if_not_found=False)

        #     if task.progress_percentage == 100 and task.stage_id and done_stage and task.stage_id.id != done_stage.id:
        #         task.stage_id = done_stage.id

        #     if task.stage_id and done_stage and task.stage_id.id == done_stage.id and task.progress_percentage < 100:
        #         raise ValidationError("Task in 'Done' stage must have 100% progress.")
            

        # Third Method
        for task in self:
            if task.progress_percentage == 100 and task.stage_id and task.stage_id.id != "3":
                
                done_stage = self.env["project.task.type"].search(
                    [("id", "=", "3"),
                    #  ("project_ids", "in", [task.project_id.id])
                     ], limit=1
                )
                print("\n\n\n\n--------->0000000",done_stage)
                print("\n\n\n\n--------->111111",task.stage_id)
                if done_stage:
                    task.stage_id = done_stage.id

            if task.stage_id and task.stage_id.id == "3" and task.progress_percentage < 100:
                raise ValidationError("Task in 'Done' stage must have 100% progress.")