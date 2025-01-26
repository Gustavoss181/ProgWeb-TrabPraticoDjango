from django.urls import path
from . import views

urlpatterns = [
    path('carrinho/', views.ver_carrinho, name='ver_carrinho'),
    path('carrinho/finalizar/', views.finalizar_pedido, name='finalizar_pedido'),
    path('pedidos/<int:pedido_id>/', views.detalhes_pedido, name='detalhes_pedido'),
]