from odoo import fields, models, api

class TodoList(models.Model):
    _name = "owl.todolist"
    _description = "OWL Todo List Application"

    name = fields.Char(string="Task Name")
    completed = fields.Boolean(string="Complete?")
    color = fields.Char(string="Task Color")