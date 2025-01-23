from .models import InstrumentoCorda, InstrumentoSopro, InstrumentoPercussao

def tipos_instrumentos(request):
    tipos_corda = [tipo[0] for tipo in InstrumentoCorda._meta.get_field('tipo_instrumento').choices]
    tipos_sopro = [tipo[0] for tipo in InstrumentoSopro._meta.get_field('tipo_instrumento').choices]
    tipos_percussao = [tipo[0] for tipo in InstrumentoPercussao._meta.get_field('tipo_instrumento').choices]

    return {
        'tipos_corda': tipos_corda,
        'tipos_sopro': tipos_sopro,
        'tipos_percussao': tipos_percussao,
    }
