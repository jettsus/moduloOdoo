# -*- coding: utf-8 -*-
# from odoo import http


# class SalidasAlumnos(http.Controller):
#     @http.route('/salidas_alumnos/salidas_alumnos', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/salidas_alumnos/salidas_alumnos/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('salidas_alumnos.listing', {
#             'root': '/salidas_alumnos/salidas_alumnos',
#             'objects': http.request.env['salidas_alumnos.salidas_alumnos'].search([]),
#         })

#     @http.route('/salidas_alumnos/salidas_alumnos/objects/<model("salidas_alumnos.salidas_alumnos"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('salidas_alumnos.object', {
#             'object': obj
#         })

