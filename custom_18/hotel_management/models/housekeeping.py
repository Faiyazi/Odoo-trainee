from odoo import api, fields, models

class HousekeepingTask(models.Model):
    _name = "hotel.housekeeping.task"
    _description = "Housekeeping Task"
    _inherit = ["mail.thread","mail.activity.mixin"]

    name = fields.Char(required=True)
    room_id = fields.Many2one("hotel.room", required=True)
    assigned_user_id = fields.Many2one("res.users")
    date = fields.Date(default=fields.Date.today)
    state = fields.Selection([("todo","To Do"),("in_progress","In Progress"),("done","Done")], default="todo", tracking=True)

    @api.model
    def cron_generate_tasks(self):
        dirty_rooms = self.env["hotel.room"].search([("state","=","dirty")])
        for room in dirty_rooms:
            exists = self.search_count([("room_id","=",room.id),("state","!=","done"),("date","=",fields.Date.today())])
            if not exists:
                self.create({"name": f"Clean: {room.name}", "room_id": room.id})
