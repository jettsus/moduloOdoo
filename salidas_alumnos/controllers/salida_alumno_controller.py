from odoo import http
from odoo.http import request

class SalidaAlumnoController(http.Controller):

    @http.route('/salida_alumno/autorizados', type='json', auth='user')
    def obtener_autorizados(self):
        autorizados = request.env['salida.alumno'].search([('autorizado', '=', True)])
        return [{'id': alumno.id, 'nombre': alumno.alumno_id.name} for alumno in autorizados]

    @http.route('/salida_alumno/autorizar', type='json', auth='user')
    def autorizar_salida(self, alumno_id):
        alumno = request.env['salida.alumno'].search([('alumno_id', '=', alumno_id)])
        if alumno:
            alumno.autorizado = True
        return {'success': True}

    @http.route('/salida_alumno/revocar', type='json', auth='user')
    def revocar_salida(self, alumno_id):
        alumno = request.env['salida.alumno'].search([('alumno_id', '=', alumno_id)])
        if alumno:
            alumno.autorizado = False
        return {'success': True}
