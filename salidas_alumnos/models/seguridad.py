from odoo import models, fields

class SeguridadSalidaAlumno(models.Model):
    _name = 'salida.alumno.seguridad'
    _description = 'Permisos de acceso a control de salidas'

    user_id = fields.Many2one('res.users', string='Usuario', required=True)
    puede_ver = fields.Boolean(string='Puede ver salidas', default=False)
    puede_editar = fields.Boolean(string='Puede editar salidas', default=False)
    puede_borrar = fields.Boolean(string='Puede borrar salidas', default=False)
