from odoo import fields,models

class Consultation_virtual_meet(models.Model):
    _name="consultaion.real.meet"
    _description = "This is to have consultation in an offline meet"

    customer_name = fields.Char(required=True)
    property_type=fields.Selection(
        string='Property Type',
        selection=[('flats','Flats'),('villa','Villa'),('penthouse','Penthouse')],
        required=True,
        default='flats'
    )
    property_painting = fields.Boolean()
    property_coloring = fields.Boolean() 
