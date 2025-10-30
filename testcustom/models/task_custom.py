from odoo import models, fields

class TaskCustom(models.Model):
    _name = 'task.custom'
    _description = 'Custom Task'
    _inherits = {'project.task': 'task_id'}
                 
    name = fields.Char(string='Task Name', required=True ,translate=True)
    description = fields.Text(string='Description')
    active = fields.Boolean(string='Active', default=True)
    age = fields.Integer(string="age")

    task_id = fields.Many2one('project.task', required=True, ondelete='cascade')
    status = fields.Selection([('new','New'),('inprogress','INPROGRESS'),('finish','FINISH')])