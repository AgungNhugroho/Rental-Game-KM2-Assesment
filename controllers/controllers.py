# -*- coding: utf-8 -*-
# from odoo import http


# class Nugroho(http.Controller):
#     @http.route('/nugroho/nugroho/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/nugroho/nugroho/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('nugroho.listing', {
#             'root': '/nugroho/nugroho',
#             'objects': http.request.env['nugroho.nugroho'].search([]),
#         })

#     @http.route('/nugroho/nugroho/objects/<model("nugroho.nugroho"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('nugroho.object', {
#             'object': obj
#         })
