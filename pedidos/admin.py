from django.contrib import admin
from .models import Pedido, PedidoProduto

# Register your models here.
admin.site.register(Pedido)
admin.site.register(PedidoProduto)