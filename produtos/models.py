from django.db import models

# Create your models here.
class Categoria(models.Model):
    nome = models.CharField(max_length=50, unique=True)
    descricao = models.TextField()

    def __str__(self):
        return self.nome

class Guitarra(models.Model):
    nome = models.CharField(max_length=100)
    marca = models.CharField(max_length=50)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    estoque = models.IntegerField()
    descricao = models.TextField()
    # imagem = models.ImageField(upload_to='guitarras/')
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name='guitarras', default=1)

    def __str__(self):
        return self.nome