from django.conf.urls import include, url
from . import views
from django.conf.urls.static import static
from ReguU3 import settings
from django.contrib.auth.views import login, logout_then_login
from django.views.static import serve

urlpatterns = [
    url(r'^$', views.index),
    url(r'^index/$', views.index, name="index"),
    url(r'^perfil/$', views.perfil, name="perfil"),
    url(r'^login/$', login, {'template_name': 'login.html'}, name='login'),
    url(r'^logout/$', logout_then_login, name='logout'),
    url(r'^signup/$', views.SignUp.as_view(),name="signup"),
    url(r'usuarios/$', views.usuarios, name="usuarios_view"),
]

if settings.DEBUG is True:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
