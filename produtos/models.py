from django.db import models

# Create your models here.
class Produto(models.Model):
    codigo = models.CharField(max_length=20, unique=True)  # Código único do produto
    quantidade = models.PositiveIntegerField(default=0)  # Quantidade em estoque
    preco = models.DecimalField(max_digits=10, decimal_places=2)  # Preço do produto
    # foto = models.ImageField(upload_to='produtos/', blank=True, null=True)
    foto = models.URLField(blank=True, null=True)

    def get_nome(self):
        if hasattr(self, 'produto_instrumento'):
            instrumento = self.produto_instrumento
            if instrumento.instrumento_corda:
                return str(instrumento.instrumento_corda)
            elif instrumento.instrumento_sopro:
                return str(instrumento.instrumento_sopro)
            elif instrumento.instrumento_percussao:
                return str(instrumento.instrumento_percussao)
        return "Sem nome"

    def __str__(self):
        return f"{self.codigo} - R${self.preco}"

class InstrumentoCorda(models.Model):
    TIPO_INSTRUMENTO_CHOICES = [
        ('guitarra', 'Guitarra'),
        ('violao', 'Violão'),
        ('baixo', 'Baixo'),
    ]

    modelo = models.CharField(max_length=100)
    serie = models.CharField(max_length=50, blank=True, null=True)
    numero_trastes = models.PositiveIntegerField()
    numero_cordas = models.PositiveIntegerField()
    captadores = models.CharField(max_length=100, blank=True, null=True)
    tipo_corpo = models.CharField(
        max_length=50,
        choices=[
            ('classico', 'Clássico'),
            ('folk', 'Folk'),
            ('jumbo', 'Jumbo'),
            ('flat', 'Flat'),
            ('outros', 'Outros'),
        ],
        blank=True,
        null=True
    )
    cor = models.CharField(max_length=30)
    tipo_instrumento = models.CharField(max_length=50, choices=TIPO_INSTRUMENTO_CHOICES)

    def __str__(self):
        return f"{self.tipo_instrumento} - {self.modelo}"

class InstrumentoSopro(models.Model):
    TIPO_INSTRUMENTO_CHOICES = [
        ('flauta', 'Flauta'),
        ('clarinete', 'Clarinete'),
        ('saxofone', 'Saxofone'),
        ('trompete', 'Trompete'),
        ('trombone', 'Trombone'),
        ('oboé', 'Oboé'),
    ]
    ALCANCE_CHOICES = [
        ('baixo', 'Baixo'),
        ('alto', 'Alto'),
        ('tenor', 'Tenor'),
    ]

    MATERIAL_CHOICES = [
        ('metal', 'Metal'),
        ('madeira', 'Madeira'),
    ]

    material = models.CharField(max_length=50, choices=MATERIAL_CHOICES)
    alcance = models.CharField(max_length=50, choices=ALCANCE_CHOICES)
    tipo_bocal = models.CharField(max_length=50)
    quantidade_valvulas = models.PositiveIntegerField()
    afinacao = models.CharField(max_length=50)
    tipo_instrumento = models.CharField(max_length=50, choices=TIPO_INSTRUMENTO_CHOICES)

    def __str__(self):
        return f"{self.tipo_instrumento} - {self.material} ({self.alcance})"

class InstrumentoPercussao(models.Model):
    TIPO_INSTRUMENTO_CHOICES = [
        ('tambor', 'Tambor'),
        ('timbal', 'Timbal'),
        ('xilofone', 'Xilofone'),
        ('maracas', 'Maracas'),
        ('triangulo', 'Triângulo'),
        ('caixa', 'Caixa'),
    ]
    MATERIAL_CHOICES = [
        ('madeira', 'Madeira'),
        ('metal', 'Metal'),
        ('sintetico', 'Sintético'),
    ]

    material = models.CharField(max_length=50, choices=MATERIAL_CHOICES)
    altura = models.PositiveIntegerField()
    tipo_percussao = models.CharField(max_length=50)  # Ex.: Tímpano, Caixa, etc.
    diametro = models.PositiveIntegerField()
    altura_casca = models.PositiveIntegerField()
    tipo_instrumento = models.CharField(max_length=50, choices=TIPO_INSTRUMENTO_CHOICES)

    def __str__(self):
        return f"{self.tipo_instrumento} - {self.material} ({self.altura}cm)"
    

class ProdutoInstrumento(models.Model):
    produto = models.OneToOneField(Produto, on_delete=models.CASCADE, related_name="produto_instrumento")
    instrumento_corda = models.OneToOneField(
        InstrumentoCorda, on_delete=models.SET_NULL, null=True, blank=True, related_name="produto_corda"
    )
    instrumento_sopro = models.OneToOneField(
        InstrumentoSopro, on_delete=models.SET_NULL, null=True, blank=True, related_name="produto_sopro"
    )
    instrumento_percussao = models.OneToOneField(
        InstrumentoPercussao, on_delete=models.SET_NULL, null=True, blank=True, related_name="produto_percussao"
    )

    def save(self, *args, **kwargs):
        # Garante que apenas um tipo de instrumento está relacionado
        instrumentos = [self.instrumento_corda, self.instrumento_sopro, self.instrumento_percussao]
        if sum(1 for instrumento in instrumentos if instrumento is not None) > 1:
            raise ValueError("Um produto pode estar associado a apenas um tipo de instrumento!")
        super().save(*args, **kwargs)

    def __str__(self):
        tipo = "Indefinido"
        if self.instrumento_corda:
            tipo = "Corda"
        elif self.instrumento_sopro:
            tipo = "Sopro"
        elif self.instrumento_percussao:
            tipo = "Percussão"
        return f"{self.produto.codigo} - Tipo: {tipo}"