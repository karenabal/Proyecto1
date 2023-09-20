from django.db import models
from django.contrib.auth.models import User

# Modelo para Profesores
class Profesor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    especialidad = models.CharField(max_length=100)
    avatar = models.FileField(default='default.jpg', upload_to='profesor_avatares')

class Meta:
    app_label = 'Proyecto_principal'

    def __str__(self):
        return self.user.username

# Modelo para Alumnos
class Alumno(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    fecha_nacimiento = models.DateField()
    avatar = models.FileField(default='default.jpg', upload_to='alumno_avatares')
   

    def __str__(self):
        return self.user.username

# Modelo para Cursos
class Curso(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField()
    profesor = models.ForeignKey(Profesor, on_delete=models.CASCADE)
    alumnos = models.ManyToManyField(Alumno, blank=True)
   

    def __str__(self):
        return self.nombre

#Modelo para Usuarios


from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

class Usuario(AbstractUser):
    es_administrador = models.BooleanField(default=False)
    es_profesor = models.BooleanField(default=False)
    es_alumno = models.BooleanField(default=False)
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)

    # Relación con grupos
    groups = models.ManyToManyField(
        Group,
        verbose_name=('groups'),
        blank=True,
        related_name='usuarios'  # Agrega un related_name personalizado
    )

    # Relación con permisos de usuario
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name=('user permissions'),
        blank=True,
        related_name='usuarios'  # Agrega un related_name personalizado
    )


    def __str__(self):
        return self.username
