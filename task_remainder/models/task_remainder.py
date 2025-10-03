from datetime import timedelta
from odoo import models, fields, api


class ProjectTask(models.Model):
    _inherit = 'project.task'

    is_active = fields.Boolean(string='Active')

    @api.model
    def send_daily_remainders(self):
        today = fields.Date.today()
        tomorrow = today + timedelta(days=1)

        tasks = self.env['project.task'].search([
            ("date_deadline", ">=", today - timedelta(days=1)),
        ])


        for task in tasks:

            if task.is_active== False:
                if not task.date_deadline:
                    continue

                deadline_date = task.date_deadline.date()

                for user in task.user_ids:
                    subject, body = None, None

                    if deadline_date == today:
                        subject = f"Task Due Today: {task.name}"
                        body = f"Reminder: Your task '{task.name}' is due today ({deadline_date})."
                    elif deadline_date == tomorrow:
                        subject = f"Task Due Tomorrow: {task.name}"
                        body = f"Reminder: Your task '{task.name}' is due tomorrow ({deadline_date})."

                    self.env["mail.mail"].sudo().create([{
                    "subject": "Daily Timesheet Summary",
                    "body_html": f"<p>{body}</p>",
                    "email_to": user.email,
                    'auto_delete': True
                    }]).send()

