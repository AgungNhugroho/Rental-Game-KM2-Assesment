from odoo import api, fields, models


class publisher(models.Model):
    _name = 'rental.publisher'
    _description = 'Console Class Publisher'

    name = fields.Char(string='Nama')
    region = fields.Char(string='Region')
    code_region = fields.Char(string='Code Region')
    