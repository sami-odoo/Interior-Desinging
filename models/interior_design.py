#-*- coding -*-

from odoo import fields,models

class Interior_desigining(models.Model):
    _name="design.interior"
    _description="App for interior designing"


    name=fields.Char(required=True)
    property_type=state=fields.Selection(
        string='Property Type',
        selection=[('flats','Flats'),('villa','Villa'),('penthouse','Penthouse')],
        required=True,
        copy=False,
        default='flats'
    )
    painting = fields.Boolean()
    coloring = fields.Boolean() 

    