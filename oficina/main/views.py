from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from clientes.models import CadastroCliente
# Create your views here.
@login_required
def index(request):
    clientes = CadastroCliente.objects.count()
    context = {'clientes_cadastrados': clientes}
    return render(request, 'main/index.html', context)
