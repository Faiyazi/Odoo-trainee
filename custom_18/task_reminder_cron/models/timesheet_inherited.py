from odoo import models, fields, api
from datetime import date, timedelta


class TimesheetInherit(models.Model):
    _inherit = 'account.analytic.line'
    _description = 'Timesheet Inherit'

    def cron_project_timesheet_entry(self):

        today = fields.Date.today()

        timesheet=self.search([
            ("date", "=",today)
        ])

        template=self.env.ref("task_reminder_cron.email_template_timesheet_reminder",raise_if_not_found=False)

        for time in  timesheet:
            if time:
                template.send_mail(time.id,force_send=True)




