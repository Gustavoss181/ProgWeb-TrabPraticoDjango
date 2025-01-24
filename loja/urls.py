from django.urls import path
from . import views

app_name = 'loja'

urlpatterns = [
    path('', views.home, name='home'),
    path('buscar-produtos/', views.buscar_produtos, name='buscar_produtos'),
]