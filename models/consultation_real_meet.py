from odoo import fields,models,api

class Consultation_virtual_meet(models.Model):
    _name="consultaion.real.meet"
    _description = "This is to have consultation in an offline meet"
    _rec_name="customer_name"

    customer_name = fields.Char(required=True)
    type_id = fields.Many2one("interior.design.property.type")
    property_painting = fields.Boolean(default=False)
    property_furnishing = fields.Boolean(default=False)
    painting_price = fields.Float(compute="_compute_painting")
    furnishing_price = fields.Float(compute="_compute_furnishing")
    total_cost = fields.Float(compute="_compute_total_cost",default=0)

    @api.depends('property_painting')
    def _compute_painting(self):

        for record in self:
            if record.property_painting:
                record.painting_price=500
            else:
                record.painting_price=0

    @api.depends('property_furnishing')
    def _compute_furnishing(self):

        for record in self:
            if record.property_furnishing:
                record.furnishing_price=1000
            else:
                record.furnishing_price=0

    @api.depends('property_painting','property_furnishing')
    def _compute_total_cost(self):
        
        for record in self:
            if record.property_painting:
                record.total_cost =1500 - record.furnishing_price

            elif record.property_furnishing:
                record.total_cost =1500 -  record.painting_price

            elif record.property_painting and record.property_furnishing:
                record.total_cost = 1500
            else:
                record.total_cost=0.00