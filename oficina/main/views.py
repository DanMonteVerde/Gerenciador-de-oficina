from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from clientes.models import CadastroCliente
from veiculos.models import Veiculo
from servicos.models import CadrastroServicos
# Create your views here.
@login_required
def index(request):
    clientes = CadastroCliente.objects.count()
    context = {'clientes_cadastrados': clientes, 'veiculos_em_manutencao': CadrastroServicos.quantidade_em_andamento(), 'servicos_concluidos': CadrastroServicos.quantidade_concluidos(), 'total_servicos': CadrastroServicos.objects.all()}
    return render(request, 'main/index.html', context)
