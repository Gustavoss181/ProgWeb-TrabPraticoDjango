from django.db import models

# Create your models here.
class Produto(models.Model):
    unique_id = models.AutoField(primary_key=True)
    codigo = models.CharField(max_length=100, unique=True)  # Garantindo unicidade
    quantidade = models.PositiveIntegerField()
    preco = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.codigo

# Guitarra
class Guitarra(models.Model):
    unique_id = models.AutoField(primary_key=True)
    produto = models.OneToOneField(Produto, on_delete=models.CASCADE, related_name="guitarra")
    modelo = models.CharField(max_length=100)
    serie = models.CharField(max_length=100, unique=True)  # Garantindo unicidade
    numero_trastes = models.PositiveIntegerField()
    numero_cordas = models.PositiveIntegerField()
    captadores = models.CharField(max_length=100)
    cor = models.CharField(max_length=50)

    def __str__(self):
        return self.modelo

# Violão
class Violao(models.Model):
    TIPOS_CORDA = [
        ('nylon', 'Nylon'),
        ('aco', 'Aço'),
    ]

    TIPOS_CORPO = [
        ('classico', 'Clássico'),
        ('folk', 'Folk'),
        ('jumbo', 'Jumbo'),
        ('flat', 'Flat'),
        ('outros', 'Outros'),
    ]

    unique_id = models.AutoField(primary_key=True)
    produto = models.OneToOneField(Produto, on_delete=models.CASCADE, related_name="violao")
    modelo = models.CharField(max_length=100)
    serie = models.CharField(max_length=100, unique=True)  # Garantindo unicidade
    numero_trastes = models.PositiveIntegerField()
    numero_cordas = models.PositiveIntegerField()
    tipo_corpo = models.CharField(max_length=10, choices=TIPOS_CORPO)
    tipo_corda = models.CharField(max_length=10, choices=TIPOS_CORDA)
    cor = models.CharField(max_length=50)

    def __str__(self):
        return self.modelo

# Baixo
class Baixo(models.Model):
    unique_id = models.AutoField(primary_key=True)
    produto = models.OneToOneField(Produto, on_delete=models.CASCADE, related_name="baixo")
    modelo = models.CharField(max_length=100)
    serie = models.CharField(max_length=100, unique=True)  # Garantindo unicidade
    numero_trastes = models.PositiveIntegerField()
    numero_cordas = models.PositiveIntegerField()
    captadores = models.CharField(max_length=100)
    cor = models.CharField(max_length=50)

    def __str__(self):
        return self.modelo