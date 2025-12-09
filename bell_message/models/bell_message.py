from odoo import models, fields


class Bellmessage(models.Model):
    _name = "x.alert"
    _description = "Alert Notifications"
    _rec_name = "title"

    title = fields.Char(string="Title", required=True)
    message = fields.Char(string="Message")
    is_read = fields.Boolean(string="Read", default=False)
