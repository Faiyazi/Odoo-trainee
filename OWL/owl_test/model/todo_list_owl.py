from odoo import models,fields


class TodoList(models.Model):
    _name = 'todo.list.owl'
    _description='Owl Todo List'
    
    name = fields.Char(string='Name',required=True)
    completed = fields.Boolean()
    color = fields.Char()