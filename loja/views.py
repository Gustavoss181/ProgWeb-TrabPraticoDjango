from django.shortcuts import render
from django.db.models import Q
from produtos.models import Produto, InstrumentoCorda, InstrumentoSopro, InstrumentoPercussao

# Create your views here.
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

    tipos_corda = [tipo[0] for tipo in InstrumentoCorda._meta.get_field('tipo_instrumento').choices]
    tipos_sopro = [tipo[0] for tipo in InstrumentoSopro._meta.get_field('tipo_instrumento').choices]
    tipos_percussao = [tipo[0] for tipo in InstrumentoPercussao._meta.get_field('tipo_instrumento').choices]


    return render(request, 'loja/home.html', {
        'produtos': produtos,
        'query': query,
        'tipo': tipo,
        'tipos_corda': tipos_corda,
        'tipos_sopro': tipos_sopro,
        'tipos_percussao': tipos_percussao,
    })