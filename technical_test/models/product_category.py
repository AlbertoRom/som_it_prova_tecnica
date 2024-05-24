from odoo import fields, models


class ProductCategory(models.Model):
    _name = "product.category"
    _inherit = "product.category"

    code = fields.Char(string="Code", help="Category's Code")
