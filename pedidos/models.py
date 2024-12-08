from django.db import models

from produtos.models import Produto
from usuarios.models import Usuario

# Create your models here.
class Pedido(models.Model):
    unique_id = models.AutoField(primary_key=True)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name="pedidos")
    data_pedido = models.DateTimeField(auto_now_add=True)
    valor_total = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    def __str__(self):
        return f"Pedido {self.unique_id} - Usuário {self.usuario.username}"

    def calcular_valor_total(self):
        total = sum(item.quantidade * item.preco_unitario for item in self.itens.all())
        self.valor_total = total
        self.save()

class PedidoProduto(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE, related_name="itens_pedido")
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE, related_name="itens")
    quantidade = models.PositiveIntegerField()
    preco_unitario = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        unique_together = ("produto", "pedido")  # Garante que o mesmo produto não apareça duas vezes no mesmo pedido

    def __str__(self):
        return f"Produto {self.produto.codigo} no Pedido {self.pedido.unique_id}"