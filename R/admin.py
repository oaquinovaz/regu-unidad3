from django.contrib import admin
from .models import Usuarios, Comentarios, Respuestas

# Register your models here.
admin.site.register(Usuarios)
admin.site.register(Comentarios)
admin.site.register(Respuestas)
