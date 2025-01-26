from pyexpat.errors import messages
from django.shortcuts import get_object_or_404, render, redirect
from produtos.models import Produto
from django.contrib.auth.decorators import login_required
from .models import Pedido, PedidoProduto

@login_required
def ver_carrinho(request):
    # Recupera o carrinho da sessão
    carrinho = request.session.get('carrinho', {})
    itens_carrinho = []

    # Preenche a lista de itens do carrinho com os dados dos produtos
    for produto_id, item in carrinho.items():
        produto = Produto.objects.get(id=produto_id)
        itens_carrinho.append({
            'produto': produto,
            'quantidade': item['quantidade'],
            'preco_total': item['quantidade'] * item['preco'],
        })

    # Calcula o valor total do carrinho
    valor_total = sum(item['preco_total'] for item in itens_carrinho)

    return render(request, 'pedidos/ver_carrinho.html', {
        'itens_carrinho': itens_carrinho,
        'valor_total': valor_total,
    })

@login_required
def finalizar_pedido(request):
    carrinho = request.session.get('carrinho', {})

    if not carrinho:
        messages.error(request, "Seu carrinho está vazio.")
        return redirect('ver_carrinho')

    # Cria um novo pedido
    pedido = Pedido.objects.create(
        usuario=request.user,
        valor_total=0,
    )

    # Adiciona os itens do carrinho ao pedido
    for produto_id, item in carrinho.items():
        produto = Produto.objects.get(id=produto_id)
        PedidoProduto.objects.create(
            pedido=pedido,
            produto=produto,
            quantidade=item['quantidade'],
            preco_unitario=item['preco'],
        )

    # Calcula o valor total do pedido
    pedido.calcular_valor_total()

    # Limpa o carrinho da sessão
    request.session['carrinho'] = {}

    # Redireciona para a página de detalhes do pedido
    return redirect('detalhes_pedido', pedido_id=pedido.unique_id)

def detalhes_pedido(request, pedido_id):
    pedido = get_object_or_404(Pedido, unique_id=pedido_id)
    itens_com_total = []

    # Calcula o total de cada item
    for item in pedido.itens.all():
        item.total = item.quantidade * item.preco_unitario
        itens_com_total.append(item)

    return render(request, 'pedidos/detalhes_pedido.html', {
        'pedido': pedido,
        'itens_com_total': itens_com_total,
    })