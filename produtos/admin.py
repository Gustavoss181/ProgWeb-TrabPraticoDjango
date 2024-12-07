from django.contrib import admin
from .models import Guitarra, Violao, Baixo, Produto

# Register your models here.
admin.site.register(Produto)
admin.site.register(Guitarra)
admin.site.register(Violao)
admin.site.register(Baixo)