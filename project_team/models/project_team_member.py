from odoo import models, fields, api
from odoo.exceptions import ValidationError


class TeamMember(models.Model):
    _name = "project.team.member"
    _description = "Project Team Member"
    _rec_name = "name"

    user_id = fields.Many2one(
        "res.users",
        string="User",
        context={"search_default_employee": 1},
        domain="[('employee_id', '!=', False)]",
    )
    seq = fields.Integer(string="sequence", default="10")
    # User details
    name = fields.Char(string="Name", required=True, help="Enter your name")
    email = fields.Char(
        string="Email", related="user_id.email", readonly=False, store=True
    )
    mobile = fields.Char(string="Mobile No",size=10)
    member_ids = fields.Many2many("project.team", "team_id", string="Team")
    gender = fields.Selection(
        [("male", "Male"), ("female", "Female"), ("others", "Others")], default=""
    )
    dob = fields.Date(string="Birth Day")
    image_128 = fields.Binary(string="Image", store=True)

    # user address
    address = fields.Char(string="Address")
    house_no = fields.Char(string="House No")
    street = fields.Char(string="Street")
    street2 = fields.Char(string="Street2")
    country_id = fields.Many2one("res.country", string="Country")
    state_id = fields.Many2one("res.country.state", string="State")
    city = fields.Many2one("res.state.city", string="City")
    zip_code = fields.Char(string="Zip Code")

    bio_data = fields.Html(string="Bio data")
    description = fields.Text(string="Description", index=True)
    # Index help to search and filter the data for database

    timesheet_ids = fields.One2many(
        comodel_name="account.analytic.line",
        inverse_name="time_sheet_id",
        string="Timesheets",
    )

    is_active = fields.Boolean(string="Active", default=True)
  

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            existing_user = False  # always initialize

            if not vals.get("user_id") and vals.get("email"):
                existing_user = self.env["res.users"].search(
                    [("login", "=", vals.get("email"))], limit=1
                )

            # if existing_user:
            #     vals['user_id'] = existing_user.id
            if not vals["user_id"]:
                new_user = self.env["res.users"].create(
                    {
                        "name": vals["name"],
                        "login": vals["email"],
                        "email": vals["email"],
                    }
                )
                vals["user_id"] = new_user.id

        return super().create(vals_list)


    def copy(self):
        raise ValidationError("This model can't be copied")

    @api.constrains("mobile","name")
    def contact(self):
        for rec in self:
            # if len(rec.mobile) != 10  :
            #     raise ValidationError('Its length should be 10')

            # if not rec.mobile.isdigit():
            #     raise ValidationError("Its should be Number ")
            
            
            if rec.name.lower():
                domain = [
                    ("name", "=", rec.name),
                    ("id", "!=", rec.id),
                ]
                if self.search_count(domain):
                    raise ValidationError("Name already exists")
