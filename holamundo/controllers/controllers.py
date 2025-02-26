# -*- coding: utf-8 -*-
# from odoo import http


# class Holamundo(http.Controller):
#     @http.route('/holamundo/holamundo', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/holamundo/holamundo/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('holamundo.listing', {
#             'root': '/holamundo/holamundo',
#             'objects': http.request.env['holamundo.holamundo'].search([]),
#         })

#     @http.route('/holamundo/holamundo/objects/<model("holamundo.holamundo"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('holamundo.object', {
#             'object': obj
#         })

