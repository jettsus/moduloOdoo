# Control de Salidas a Mayores de 18 Años

## Descripción
"Control de Salidas a Mayores de 18 Años" es un módulo desarrollado en Odoo para el Instituto Cañada de la Encina de Iniesta, diseñado para supervisar las salidas de alumnos durante recreos o entre horas, especialmente para aquellos mayores de edad o con autorización parental. Este módulo permite al personal de conserjería consultar una lista de alumnos autorizados a salir en un momento determinado, filtrando por fecha, curso y grupo, y buscar por campos específicos de los alumnos (como DNI). Además, facilita la inserción y eliminación de alumnos, integrándose con otra aplicación del centro (Alumnos o Personal) para obtener los datos, sin almacenarlos localmente. El objetivo es agilizar la verificación de autorizaciones de salida y mejorar la gestión del centro educativo.

## Funcionalidades
- **Consulta de Alumnos Autorizados:** Formulario y vista Kanban con miniaturas de alumnos autorizados, mostrando si tienen permiso para salir (verde para autorizados).
- **Filtrado y Búsqueda:** Filtra por curso, grupo y fecha, y busca por campos del alumno.
- **Gestión de Alumnos:** Permite insertar y eliminar alumnos desde una vista de formulario.
- **Seguridad:** Permisos restringidos al grupo "Conserjes" para garantizar acceso exclusivo.
- **Integración:** Se conecta con otra aplicación del centro para obtener datos de alumnos.

## Tecnologías
- **Plataforma:** Odoo (versión compatible: 16/17)
- **Lenguajes:** Python (lógica y modelos), XML (vistas y modelos)
- **Metodología:** Kanban (gestión ágil del proyecto)
- **Base de Datos:** PostgreSQL (integrada con Odoo)

## Instalación
1. Clona el repositorio: `git clone https://github.com/jettsus/moduloOdoo.git`
2. Copia la carpeta `salidas_alumnos` en el directorio `addons` de tu instalación de Odoo o una nueva que tengas y añade la ruta al path:
addons_path = c:\program files\odoo 17.0.20240418\server\odoo\addons,(C:\Archivos de programa\Odoo 17.0.20240418\server\MisModulos)
la segunda ruta es donde se meten el modulo.

3. Reinicia el servidor de Odoo: `sudo systemctl restart odoo` (o el comando correspondiente).
4. Inicia sesión en Odoo, ve a "Aplicaciones", busca "salidas_alumnos" y haz clic en "Instalar".
5. Configura los permisos para el grupo "Conserjes" desde Odoo (modo desarrollador > Modelos).

## Uso
1. Accede al módulo desde el menú "Gestión de Salidas" > "Control de Salidas".
2. Usa la vista Kanban para identificar alumnos autorizados (verde = autorizado).
3. Filtra por curso, grupo o fecha o nombre.
4. Añade nuevos alumnos desde la vista de formulario (botón "Nuevo").
5. Elimina o edita alumnos según sea necesario.

## Cómo Contribuir
- Reporta problemas o sugerencias en la pestaña de [Issues](https://github.com/jettsus/control-salidas-odoo/issues).
- Envía pull requests con mejoras.

## Futuras Mejoras
- Marcar en rojo a los alumnos no autorizados.
- Exportar datos de grupos para análisis pero debe ser en la vista lista.

## Contacto
- **Autor:** [jettsus](mailto:jettsusc0c@gmail.com)
- **Repositorio:** [GitHub](https://github.com/jettsus/moduloOdoo)
