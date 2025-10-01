from odoo import models, fields, api
from datetime import datetime, date, timedelta


class ProjectTaskInherit(models.Model):
    _inherit = 'project.task'
    _description = 'Project Task Inherit'

    def cron_project_task_reminder(self):
        today = datetime.today()
        tomorrow = date.today() + timedelta(days=1)

        tasks= self.search([("date_deadline", "in",[today,tomorrow])])

        template=self.env.ref("task_reminder_cron.email_template_task_reminder",raise_if_not_found=False)

        for task in tasks:
            if template:
                template.send_mail(task.id,force_send=True)

