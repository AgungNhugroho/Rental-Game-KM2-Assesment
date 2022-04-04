from odoo import api, fields, models


class pengembalian(models.Model):
    _name = 'rental.pengembalian'
    _description = 'Pengembalian Barang'

    
    order = fields.Many2one(comodel_name='rental.order', string='Order')
    name = fields.Char(compute='_compute_penyewa', string='Penyewa')
    
    @api.depends('order')
    def _compute_penyewa(self):
        for record in self:
            record.name = self.env['rental.order'].search([('id', '=', record.order.id)]).mapped('pemesan').name
    balik = fields.Date('Tanggal Pengembalian', default=fields.Date.today())
    tagihan = fields.Integer(compute='_compute_tagihan', string='Tagihan')
    
    @api.depends('order')
    def _compute_tagihan(self):
        for record in self:
            record.tagihan = record.order.total
