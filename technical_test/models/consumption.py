from odoo import fields, models


class Consumption(models.Model):
    _name = "consumption"

    date = fields.Datetime(string='Date', default=fields.Datetime.now)
    product_id = fields.Many2one('product.template', string='Product')
    quantity = fields.Integer(string='Quantity')
    category = fields.Char(related="product_id.categ_id.code",
                           string='Category', store=True)
