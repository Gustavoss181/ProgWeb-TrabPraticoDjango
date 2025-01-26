from django.urls import path
from . import views
urlpatterns = [
    path('cadastro/', views.cadastro, name='cadastro'),
    path('login/', views.autenticar, name='autenticar'),
    path('', views.home, name='home')
]