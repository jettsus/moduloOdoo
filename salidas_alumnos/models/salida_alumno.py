from odoo import models, fields

class SalidaAlumno(models.Model):
    _name = 'salida.alumno'
    _description = 'Registro de salida de alumnos mayores de 18 años'

    alumno_id = fields.Many2one('res.partner', string="Alumno", required=True)
    fecha_salida = fields.Datetime(string="Fecha de salida", required=True)
    autorizado = fields.Boolean(string="Autorizado", default=True)
    curso = fields.Char(string="Curso")
    grupo = fields.Char(string="Grupo")
