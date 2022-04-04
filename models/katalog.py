from odoo import api, fields, models


class katalog(models.Model):
    _name = 'rental.katalog'
    _description = 'Katalog Rental Game'

    name = fields.Char(string='Name')
    deskripsi = fields.Char(string='Developer')
    tahun = fields.Char(string='Tahun Rilis')
    genre = fields.Char(string='Genre')
    tipe = fields.Selection(string='Tipe Game' , selection=[('Digital','Fisik'), ('Fisik','Digital')])
    harga = fields.Integer(string='Harga')
    stok = fields.Integer(string='Stok')
    