from odoo import api, fields, models


class playstation(models.Model):
    _name = 'rental.playstation'
    _description = 'Daftar Console Sony Playstation'

    name = fields.Char(string='Name')
    deskripsi = fields.Char(string='Etalase Sony Playstation')
    harga = fields.Integer(string='Harga Sewa')
    
    
    
