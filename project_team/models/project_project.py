from odoo import models,fields

class ProjectProject(models.Model):
    _inherit = 'project.project'


    team_member_id = fields.Many2many('project.team.member', string='Team Member')
    team_id = fields.Many2one('project.team',string='Teams',domain=[('is_active','=','False')])



