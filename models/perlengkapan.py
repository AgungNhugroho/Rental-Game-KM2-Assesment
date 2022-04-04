from odoo import api, fields, models


class perlengkapan(models.Model):
    _name = 'rental.perlengkapan'
    _description = 'Console Addons'

    name = fields.Char(string='Name')
    deskripsi = fields.Char(string='Tipe')
    tipe = fields.Char(string='Platform')
    harga = fields.Integer(string='harga sewa')
    
    
    
