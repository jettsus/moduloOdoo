from odoo import models, fields

class SalidaAlumno(models.Model):
    _name = 'salida.alumno'
    _description = 'Salida de Alumno'

    alumno_id = fields.Many2one('res.partner', string="Alumno", ondelete="cascade")
    fecha_salida = fields.Datetime(string="Fecha de salida", store=True)
    autorizado = fields.Boolean(string="Autorizado", default=False) 
    curso = fields.Char(string="Curso", store=True)
    grupo = fields.Char(string="Grupo", store=True)
    imagen = fields.Binary(string="Foto del Alumno", attachment=True, store=True)
