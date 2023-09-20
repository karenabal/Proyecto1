from django.urls import path
from . import views

urlpatterns = [
    # URLs para Profesores
    path('profesores/', views.lista_profesores, name='lista_profesores'),
    path('profesores/<int:profesor_id>/', views.detalle_profesor, name='detalle_profesor'),
    path('profesores/<int:profesor_id>/editar/', views.editar_profesor, name='editar_profesor'),
    path('profesores/<int:profesor_id>/eliminar/', views.eliminar_profesor, name='eliminar_profesor'),

    # URLs para Alumnos
    path('alumnos/', views.lista_alumnos, name='lista_alumnos'),
    path('alumnos/<int:alumno_id>/', views.detalle_alumno, name='detalle_alumno'),
    path('alumnos/<int:alumno_id>/editar/', views.editar_alumno, name='editar_alumno'),
    path('alumnos/<int:alumno_id>/eliminar/', views.eliminar_alumno, name='eliminar_alumno'),

    # URLs para Cursos
    path('cursos/', views.lista_cursos, name='lista_cursos'),
    path('cursos/<int:curso_id>/', views.detalle_curso, name='detalle_curso'),
    path('cursos/<int:curso_id>/editar/', views.editar_curso, name='editar_curso'),
    path('cursos/<int:curso_id>/eliminar/', views.eliminar_curso, name='eliminar_curso'),

    # URL para la vista de búsqueda
    path('buscar/', views.buscar, name='buscar'),

    # URL para la página de inicio (home)
    path('', views.home, name='home'),

    #URL para inicio sesión, cierre y registro

    path('registro/', views.registro, name='registro'),
    path('inicio_sesion/', views.inicio_sesion, name='inicio_sesion'),
    path('cierre_sesion/', views.cierre_sesion, name='cierre_sesion'),


]
