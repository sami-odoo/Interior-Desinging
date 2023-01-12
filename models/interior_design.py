#-*- coding -*-

from odoo import fields,models

class Interior_desigining(models.Model):
    _name="design.interior"
    _description="App for interior designing"


    name=fields.Char(required=True)
    