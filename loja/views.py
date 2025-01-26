from django.http import JsonResponse
from django.shortcuts import render
from django.db.models import Q
from django.urls import reverse
from produtos.models import Produto

# View principal da home
def home(request):
    query = request.GET.get('q', '')
    tipo = request.GET.get('tipo', '')
    produtos = Produto.objects.all()

    if query:
        produtos = produtos.filter(
            Q(produto_instrumento__instrumento_corda__modelo__icontains=query) |
            Q(produto_instrumento__instrumento_corda__tipo_instrumento__icontains=query) |

            Q(produto_instrumento__instrumento_sopro__tipo_instrumento__icontains=query) |

            Q(produto_instrumento__instrumento_percussao__tipo_instrumento__icontains=query)
        )
    
    if tipo:
        produtos = produtos.filter(
            Q(produto_instrumento__instrumento_corda__tipo_instrumento__iexact=tipo) |
            Q(produto_instrumento__instrumento_sopro__tipo_instrumento__iexact=tipo) |
            Q(produto_instrumento__instrumento_percussao__tipo_instrumento__iexact=tipo)
        )

    return render(request, 'loja/home.html', {
        'produtos': produtos,
        'query': query,
        'tipo': tipo,
        'usuario_logado': request.user if request.user.is_authenticated else None,
    })

# View para buscar produtos via Ajax
def buscar_produtos(request):
    query = request.GET.get('q', '')  # Captura o termo da barra de pesquisa
    if query:
        resultados = Produto.objects.filter(
            Q(produto_instrumento__instrumento_corda__modelo__icontains=query) |
            Q(produto_instrumento__instrumento_corda__tipo_instrumento__icontains=query) |

            Q(produto_instrumento__instrumento_sopro__tipo_instrumento__icontains=query) |

            Q(produto_instrumento__instrumento_percussao__tipo_instrumento__icontains=query)
        )[:5]  # Limita aos 5 primeiros
        produtos = [
            {
                'id': p.id,
                'nome': p.get_nome(),
                'url': reverse('produto_detalhe', args=[p.id]),
                'foto': p.foto
            } for p in resultados
        ]
        return JsonResponse({'produtos': produtos})
    return JsonResponse({'produtos': []})