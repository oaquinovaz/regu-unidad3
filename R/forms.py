from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Comentarios, Respuestas

class User_Form(UserCreationForm):
    imagen = forms.ImageField()
    telefono = forms.CharField(max_length=10)
    correo = forms.CharField(max_length=50)
    colonia = forms.CharField(max_length=50)

class Comentarios_Form(forms.ModelForm):
	class Meta:
		model = Comentarios
		fields = '__all__'

class Respuestas_Form(forms.ModelForm):
	class Meta:
		model = Respuestas
		fields = '__all__'
