from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save


# Create your models here.
class Usuarios(models.Model):
    id_usuario = models.AutoField(primary_key = True)
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to="fotos_perfil", default="")
    telefono = models.CharField(max_length=10)
    correo = models.CharField(max_length=50)
    colonia = models.CharField(max_length=50)

    def __str__(self):
        return self.usuario.username

class Comentarios(models.Model):
    id_comentario = models.AutoField(primary_key = True)
    usuario = models.ForeignKey(Usuarios)
    comentario = models.TextField()

    def __str__(self):
        return  str(self.id_comentario)

class Respuestas(models.Model):
    id_respuesta = models.AutoField(primary_key = True)
    id_comentario = models.ForeignKey(Comentarios, on_delete=models.CASCADE)
    usuario = models.ForeignKey(Usuarios)
    respuesta = models.TextField()

    def __str__(self):
        return str(self.id_comentario.id_comentario)
