from django.shortcuts import render
from .models import Usuarios, Comentarios, Respuestas
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse_lazy
from django.views.generic import CreateView, FormView
from .forms import User_Form
from django.core import serializers

# Create your views here.
def base(request):
    return render(request, 'base.html', {})

def index(request):
    usuarios = list(Usuarios.objects.all())
    comentarios = list(Comentarios.objects.all())
    respuestas = list(Respuestas.objects.all())
    return render(request, 'index.html', {'usuarios':usuarios ,'comentarios': comentarios, 'respuestas': respuestas})

def perfil(request):
    usuarios = list(Usuarios.objects.all())
    comentarios = list(Comentarios.objects.all())
    respuestas = list(Respuestas.objects.all())
    return render(request, 'perfil.html', {'usuarios':usuarios ,'comentarios': comentarios, 'respuestas': respuestas})

def login(request):
    return render(request, 'login.html', {})

def logout(request):
    return render(request, 'logout.html', {})

def signup(request):
    return render(request, 'signup.html', {})

class SignUp(FormView):
    template_name = 'signup.html'
    form_class = User_Form
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        user = form.save()
        p = Usuarios()
        p.usuario = user
        p.imagen = form.cleaned_data['imagen']
        p.telefono = form.cleaned_data['telefono']
        p.correo = form.cleaned_data['correo']
        p.colonia = form.cleaned_data['colonia']
        p.save()

        return super(SignUp, self).form_valid(form)

def usuarios(request):
    data = serializers.serialize('json', Usuarios.objects.all())
    return HttpResponse(data, content_type='aplication/json')
