from odoo import fields,models

class Customer_info(models.Model):
    _name="customer.info"
    _description="This is for customer information"

    name=fields.Char(required=True)
    price=fields.Float(required=True)