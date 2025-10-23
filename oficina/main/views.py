from django.shortcuts import render
# Create your views here.
def index(request):
    context = {'total_clientes': 5, 'veiculos_manutencao': 10 , 'servicos_concluidos':30, 'orcamentos_pendentes':5 }
    return render(request, 'main/index.html', context)
def teste(request):
    return render(request, 'main/teste.html')