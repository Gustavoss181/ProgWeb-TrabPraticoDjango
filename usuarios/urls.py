from django.urls import path
from . import views
urlpatterns = [
    path('cadastro/', views.cadastro, name='cadastro'),  # Página de cadastro
    path('login/', views.autenticar, name='autenticar'),  # Página de login
]