from django.shortcuts import render
from produtos.models import Produto

# Create your views here.
def home(request):
    produtos = Produto.objects.all()
    return render(request, 'loja/home.html', {'produtos': produtos})