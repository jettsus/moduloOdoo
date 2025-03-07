{
    'name': 'Control de Salidas Mayores de 18',
    'version': '1.0',
    'summary': 'Gestión de salidas de alumnos mayores de 18 años',
    'author': 'Tu Nombre',
    'category': 'Educación',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/salida_alumno_views.xml',
        'views/salida_alumno_menu.xml', 
    ],
    'installable': True,
    'application': True,
}
