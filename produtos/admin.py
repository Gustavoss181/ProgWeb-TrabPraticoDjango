from django.contrib import admin
from .models import Produto, ProdutoInstrumento, InstrumentoCorda, InstrumentoSopro, InstrumentoPercussao

admin.site.register(Produto)
admin.site.register(ProdutoInstrumento)
admin.site.register(InstrumentoCorda)
admin.site.register(InstrumentoSopro)
admin.site.register(InstrumentoPercussao)