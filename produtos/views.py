from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from produtos.models import Produto

# Create your views here.

def produto_detalhe(request, produto_id):
    produto = get_object_or_404(Produto, id=produto_id)
    return render(request, 'produtos/produto_detalhe.html', {'produto': produto})

def adicionar_ao_carrinho(request, produto_id):
    if request.method == "POST":
        quantidade = int(request.POST.get('quantidade', 1))
        # Aqui você pode implementar a lógica de adicionar ao carrinho.
        # Exemplo: salvar no banco ou na sessão
        # Para simplificar, redirecionamos de volta à página do produto.
        return HttpResponseRedirect(reverse('produto_detalhe', args=[produto_id]))