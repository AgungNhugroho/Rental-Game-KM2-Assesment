from email.policy import default
from odoo import api, fields, models


class order(models.Model):
    _name = 'rental.order'
    _description = 'New Description'
    katalogorder_ids = fields.One2many(
        comodel_name='rental.order_detail', 
        inverse_name='order_id', 
        string='Order Detail')

    gameorder_ids = fields.One2many(
        comodel_name='rental.order_gamedetail', 
        inverse_name='orderk_id', 
        string='Order Game Detail')
    
    name = fields.Char(string='kode Order', required=True)
    tanggal_order = fields.Datetime('Tanggal Order', default=fields.Datetime.now())
    tanggal_sewa = fields.Date(string='Tanggal Sewa', default=fields.Date.today())
    pemesan = fields.Many2one(
        comodel_name='res.partner', 
        string='Pemesan', 
        domain=[('is_customer','=', True)],store=True)
    total = fields.Integer(compute='_compute_total', string='Total', store=True)
    
    @api.depends('katalogorder_ids')
    def _compute_total(self):
        for record in self:
            a = sum(self.env['rental.order_detail'].search([('order_id', '=', record.id)]).mapped('harga'))
            b = sum(self.env['rental.order_gamedetail'].search([('orderk_id', '=', record.id)]).mapped('harga'))
            record.total = a + b

class orderdetail(models.Model):
    _name = 'rental.order_detail'
    _description = 'New Description'

    order_id = fields.Many2one(comodel_name='rental.order', string='Order')
    rental_id = fields.Many2one(comodel_name='rental.game', string='Item')
    
    name = fields.Selection(string='Name', selection=[('Game','game'), ('Perlengkapan','perlengkapan')])
    harga = fields.Integer(compute='_compute_harga', string='Harga')
    qty = fields.Integer(string='Quantity')
    harga_satuan = fields.Integer(compute='_compute_harga_satuan', string='harga_satuan')
    
    @api.depends('rental_id')
    def _compute_harga_satuan(self):
        for record in self:
            record.harga_satuan = record.rental_id.harga

    @api.depends('qty','harga_satuan')
    def _compute_harga(self):
        for record in self:
            record.harga = record.harga_satuan * record.qty

    @api.model
    def create(self,vals):
        record = super(orderdetail, self).create(vals)
        if record.qty:
            self.env['rental.game'].search([('id','=',record.rental_id.id)]).write({'stok':record.rental_id.stok-record.qty})
            return record
    
class ordergamedetail(models.Model):
    _name = 'rental.order_gamedetail'
    _description = 'New Description'
    
    orderk_id = fields.Many2one(comodel_name='rental.order', string='Order')
    game_id = fields.Many2one(comodel_name='rental.katalog', string='Game')
    
    name = fields.Selection(string='Name', selection=[('Game','game'), ('Perlengkapan','perlengkapan')])
    harga_satuan = fields.Integer(compute='_compute_harga_satuan', string='Harga Satuan')
    
    @api.depends('game_id')
    def _compute_harga_satuan(self):
        for record in self:
            record.harga_satuan = record.game_id.harga
    
    qty = fields.Integer(string='Quantity')
    
    harga = fields.Integer(compute='_compute_harga', string='harga')
    
    @api.depends('harga_satuan','qty')
    def _compute_harga(self):
        for record in self:
               record.harga = record.harga_satuan * record.qty
    
    @api.model
    def create(self,vals):
        record = super(ordergamedetail, self).create(vals)
        if record.qty:
            self.env['rental.katalog'].search([('id','=',record.game_id.id)]).write({'stok':record.game_id.stok-record.qty})
            return record