from odoo import fields,models

class Consultation_virtual_meet(models.Model):
    _name="consultaion.virtual.meet"
    _description = "This is to have consultation in an offline meet"

    customer_name = fields.Char(required=True)