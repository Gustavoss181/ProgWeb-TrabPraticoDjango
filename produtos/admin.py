from django.contrib import admin
from .models import Guitarra, Categoria

# Register your models here.
admin.site.register(Categoria)
admin.site.register(Guitarra)