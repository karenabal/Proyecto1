from django.shortcuts import render, redirect
from .models import Profesor
from .forms import ProfesorForm

#Vista modelo profesores

def lista_profesores(request):
    profesores = Profesor.objects.all()
    return render(request, 'lista_profesores.html', {'profesores': profesores})

def detalle_profesor(request, profesor_id):
    profesor = Profesor.objects.get(id=profesor_id)
    return render(request, 'detalle_profesor.html', {'profesor': profesor})

def editar_profesor(request, profesor_id):
    profesor = Profesor.objects.get(id=profesor_id)
    if request.method == 'POST':
        form = ProfesorForm(request.POST, request.FILES, instance=profesor)
        if form.is_valid():
            form.save()
            return redirect('lista_profesores')
    else:
        form = ProfesorForm(instance=profesor)
    return render(request, 'editar_profesor.html', {'form': form})

def eliminar_profesor(request, profesor_id):
    profesor = Profesor.objects.get(id=profesor_id)
    if request.method == 'POST':
        profesor.delete()
        return redirect('lista_profesores')
    return render(request, 'eliminar_profesor.html', {'profesor': profesor})


#Vista modelo alumnos

from django.shortcuts import render, redirect
from .models import Alumno
from .forms import AlumnoForm

def lista_alumnos(request):
    alumnos = Alumno.objects.all()
    return render(request, 'lista_alumnos.html', {'alumnos': alumnos})

def detalle_alumno(request, alumno_id):
    alumno = Alumno.objects.get(id=alumno_id)
    return render(request, 'detalle_alumno.html', {'alumno': alumno})

def editar_alumno(request, alumno_id):
    alumno = Alumno.objects.get(id=alumno_id)
    if request.method == 'POST':
        form = AlumnoForm(request.POST, request.FILES, instance=alumno)
        if form.is_valid():
            form.save()
            return redirect('lista_alumnos')
    else:
        form = AlumnoForm(instance=alumno)
    return render(request, 'editar_alumno.html', {'form': form})

def eliminar_alumno(request, alumno_id):
    alumno = Alumno.objects.get(id=alumno_id)
    if request.method == 'POST':
        alumno.delete()
        return redirect('lista_alumnos')
    return render(request, 'eliminar_alumno.html', {'alumno': alumno})


#Vista modelo cursos

from django.shortcuts import render, redirect
from .models import Curso
from .forms import CursoForm

def lista_cursos(request):
    cursos = Curso.objects.all()
    return render(request, 'lista_cursos.html', {'cursos': cursos})

def detalle_curso(request, curso_id):
    curso = Curso.objects.get(id=curso_id)
    return render(request, 'detalle_curso.html', {'curso': curso})

def editar_curso(request, curso_id):
    curso = Curso.objects.get(id=curso_id)
    if request.method == 'POST':
        form = CursoForm(request.POST, instance=curso)
        if form.is_valid():
            form.save()
            return redirect('lista_cursos')
    else:
        form = CursoForm(instance=curso)
    return render(request, 'editar_curso.html', {'form': form})

def eliminar_curso(request, curso_id):
    curso = Curso.objects.get(id=curso_id)
    if request.method == 'POST':
        curso.delete()
        return redirect('lista_cursos')
    return render(request, 'eliminar_curso.html', {'curso': curso})

from django.http import HttpResponse

def buscar(request):

    if request.GET['nombre']:
        nombre = request.GET['nombre']
        cursos = Curso.objects.filter(nombre__icontains = nombre)
        return render( request, "resultado_busqueda.html", {"cursos": cursos})
    else:
        return HttpResponse("Campo vacio")
    

    #Vista para el Home

from django.shortcuts import render

def home(request):
    return render(request, 'home.html')


#Vista para inicio de sesión, cierre y registro

from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from .forms import RegistroForm, LoginForm
from .models import Usuario

def registro(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('inicio_sesion')
    else:
        form = RegistroForm()
    return render(request, 'registro.html', {'form': form})

def inicio_sesion(request):
    if request.method == 'POST':
        form = LoginForm(request, request.POST)
        if form.is_valid():
            usuario = form.get_user()
            login(request, usuario)
            if usuario.es_administrador:
                return redirect('panel_administrador')
            elif usuario.es_profesor or usuario.es_alumno:
                return redirect('panel_usuario')
    else:
        form = LoginForm()
    return render(request, 'inicio_sesion.html', {'form': form})

def cierre_sesion(request):
    logout(request)
    return redirect('inicio')


