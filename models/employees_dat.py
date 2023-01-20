from odoo import api,models,fields

class Employees_data(models.Model):
    _name="interior.employee.dat"
    _description = "This is basically to get the information about the employee"

    name=fields.Char(required=True)
    tag_id = fields.Many2one("employee.tag")
    # cust_names = fields.One2many("")
