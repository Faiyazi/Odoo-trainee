from odoo import models, fields
from datetime import date, timedelta


class ProjectTask(models.Model):
    _inherit = 'project.task'


    ##email reminder##
    def _my_cron_method(self):
        today= fields.date.today()
        print("\n\n\n------------->today",today)
        tomorrow = today + timedelta(days=1)
        print("\n\n\n---------------->tomorrow",tomorrow)


        tasks = self.search([('date_deadline', '>=', today),
                             ('date_deadline', '<=', tomorrow)])
        print("\n\n\n----------->",tasks)
        for task in tasks:

                template = self.env.ref('deadline_reminder_task.user_task_email_template')
                template.send_mail(task.id, force_send= True)




    def _send_daily_timesheet_summary(self):
        today = fields.date.today()
        print("\n\n-------------->today",today)
        
        project_manager_group = self.env.ref('project.group_project_manager')
        managers = self.env['res.users'].search([('groups_id', 'in', project_manager_group.id)])
        print("\n\n------------------>managers",managers.name)
 
        for manager in managers:
            projects = self.env['project.project'].search([('user_id', '=', manager.id)])
            print("\n\n----------------------->projects",projects)
            if not projects:
                continue
 
            summary_lines = []
            print("\n\n----------------->summary",summary_lines)
            for rec in projects:
                timesheets = self.env['account.analytic.line'].search([
                    ('project_id', '=', rec.id),
                    ('date', '=', today)
                ])
                print("\n\n--------------->timesheets",timesheets)
                if timesheets:
                    total = sum(timesheets.mapped('unit_amount'))
                    summary_lines.append(f"{rec.name}: {total} hours")
                    print("\n\n----------->summary",summary_lines)
 
            if summary_lines:
                body = "Timesheet summary for today:\n" + "\n".join(summary_lines)
                self.env['mail.mail'].create({
                    'subject': f"Daily Timesheet Summary - {today}",
                    'body_html': f"<p>{body}</p>",
                    'email_to': manager.email,
                }).send()
 


    

            
    