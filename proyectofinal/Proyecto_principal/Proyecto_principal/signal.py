from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User

from .models import Profesor, Alumno

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        # Si es un administrador, no se crea un perfil adicional
        if instance.is_superuser:
            return

        if hasattr(instance, 'profesor'):
            Profesor.objects.create(user=instance)
        elif hasattr(instance, 'alumno'):
            Alumno.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    # Si es un administrador, no se actualiza el perfil
    if instance.is_superuser:
        return

    if hasattr(instance, 'profesor'):
        instance.profesor.save()
    elif hasattr(instance, 'alumno'):
        instance.alumno.save()
