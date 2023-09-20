# Proyecto Kursos - Plataforma Educativa

Este proyecto es una plataforma educativa desarrollada en Django que permite la gestión de profesores, alumnos, cursos y la interacción de tres tipos de usuarios: administradores, profesores y alumnos.

## Características principales

- **Herencia de HTML**: El proyecto utiliza plantillas HTML para proporcionar una apariencia uniforme en toda la aplicación.

- **Autenticación de usuarios**: Hay tres tipos de usuarios: administradores, profesores y alumnos. Los usuarios pueden iniciar sesión y acceder a funciones específicas según su rol.

- **Gestión de datos**: Los modelos de datos incluyen Profesores, Alumnos y Cursos. Los usuarios con rol de administrador pueden realizar operaciones CRUD en estos modelos.

- **Búsqueda de datos**: Los usuarios con rol de alumno tienen acceso a un formulario de búsqueda que les permite buscar información en la base de datos.

- **Control de acceso**: Los usuarios con rol de profesor pueden gestionar datos específicos de alumnos.

- **Página de inicio atractiva**: La página de inicio presenta información sobre la plataforma y los beneficios clave.

