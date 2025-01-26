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
        produto = get_object_or_404(Produto, id=produto_id)
        quantidade = int(request.POST.get('quantidade', 1))

        # Recupera o carrinho da sessão ou cria um novo
        carrinho = request.session.get('carrinho', {})

        # Adiciona o produto ao carrinho ou atualiza a quantidade
        if str(produto_id) in carrinho:
            carrinho[str(produto_id)]['quantidade'] += quantidade
        else:
            carrinho[str(produto_id)] = {
                'quantidade': quantidade,
                'preco': float(produto.preco),  # Armazena o preço como float
            }

        # Salva o carrinho na sessão
        request.session['carrinho'] = carrinho

        # Redireciona de volta para a página do produto
        return HttpResponseRedirect(reverse('produto_detalhe', args=[produto_id]))