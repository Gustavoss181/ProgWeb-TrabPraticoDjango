from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class Usuario(AbstractUser):
    # usos a serem definidos
    # endereco = models.CharField(max_length=255, blank=True, null=True)
    # telefone = models.CharField(max_length=15, blank=True, null=True)

    def __str__(self):
        return self.username