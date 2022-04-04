from odoo import api, fields, models


class Game(models.Model):
    _name = 'rental.game'
    _description = 'New Description'

    name = fields.Char(string='Name', required=True)
    playstation_id = fields.Many2one(comodel_name='rental.playstation', 
                                    string='Tipe Konsole',
                                    domain="[('harga','>','40000')]")
    perlengkapan_id = fields.Many2one(comodel_name='rental.perlengkapan', string='Tipe Addons')
    katalog_id = fields.Many2one(comodel_name='rental.katalog', string='Game')
    deskripsi = fields.Char(string='Deskripsi')
    katalogorder_ids = fields.One2many(
        comodel_name='rental.order_detail', 
        inverse_name='rental_id', 
        string='Order Detail')
    
    harga = fields.Char(compute='_compute_harga', string='Harga Sewa')
    
    @api.depends('playstation_id','perlengkapan_id','katalog_id')
    def _compute_harga(self):
        for record in self:
            record.harga = record.playstation_id.harga + record.perlengkapan_id.harga + record.katalog_id.harga
    
    stok = fields.Integer(string='Stock')
    

    
