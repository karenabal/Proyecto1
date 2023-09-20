#Form para profesor

from django import forms
from .models import Profesor


class ProfesorForm(forms.ModelForm):
    class Meta:
        model = Profesor
        fields = ['user', 'especialidad', 'avatar']  

#Form para alumno


from django import forms
from .models import Alumno

class AlumnoForm(forms.ModelForm):
    class Meta:
        model = Alumno
        fields = ['user', 'fecha_nacimiento', 'avatar']


#Form para curso

from django import forms
from .models import Curso

class CursoForm(forms.ModelForm):
    class Meta:
        model = Curso
        fields = ['nombre', 'descripcion', 'profesor', 'alumnos'] 

#Form para búsqueda

from django import forms

class BusquedaForm(forms.Form):
    nombre = forms.CharField(max_length=100, required=False)  

#Form para usuarios

from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Usuario

class RegistroForm(UserCreationForm):
    class Meta:
        model = Usuario
        fields = ['username', 'password1', 'password2', 'es_administrador', 'es_profesor', 'es_alumno', 'avatar']

class LoginForm(AuthenticationForm):
    class Meta:
        model = Usuario






