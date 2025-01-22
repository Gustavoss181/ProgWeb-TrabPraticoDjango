from django.shortcuts import render
from django.db.models import Q
from produtos.models import Produto

# Create your views here.
def home(request):
    query = request.GET.get('q', '')
    produtos = Produto.objects.all()

    if query:
        produtos = produtos.filter(
            Q(produto_instrumento__instrumento_corda__modelo__icontains=query) |
            Q(produto_instrumento__instrumento_corda__tipo_instrumento__icontains=query) |

            Q(produto_instrumento__instrumento_sopro__tipo_instrumento__icontains=query) |

            Q(produto_instrumento__instrumento_percussao__tipo_instrumento__icontains=query)
        )
    return render(request, 'loja/home.html', {'produtos': produtos, 'query': query})