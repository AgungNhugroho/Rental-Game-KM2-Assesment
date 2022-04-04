from odoo import api, fields, models


class Rental(models.Model):
    _name = 'rental.game'
    _description = 'Model Rental Game'

    name = fields.Char(string='Name Rental')
    harga = fields.Integer(string='Harga Rental')
    deskripsi = fields.Char(string='Deskripsi Rental')
    
