from django.urls import path
from . import views

urlpatterns = [
    path('<int:produto_id>/', views.produto_detalhe, name='produto_detalhe'),
    path('adicionar-ao-carrinho/<int:produto_id>/', views.adicionar_ao_carrinho, name='adicionar_ao_carrinho'),
]