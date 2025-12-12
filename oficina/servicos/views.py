from django.shortcuts import render,redirect, get_object_or_404
from .forms import CadastroServicoForm
from .models import CadrastroServicos
from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy
from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from veiculos.models import Veiculo
from clientes.models import CadastroCliente
# Create your views here.
@login_required
def index_servico(request):
    busca = request.GET.get('q', '')
    filtro = request.GET.get("filtro", "todos")

    if filtro == "agendados":
        servicos = CadrastroServicos.objects.filter(status="Pendente")
    elif filtro == "andamento":
        servicos = CadrastroServicos.objects.filter(status="Em andamento")
    elif filtro == "concluidos":
        servicos = CadrastroServicos.objects.filter(status="Concluido")
    else:
        servicos = CadrastroServicos.objects.all()
    if busca:
        servicos = servicos.filter(Q(tipo__icontains=busca) | Q(descricao__icontains=busca) | Q(data_agendamento__icontains=busca) | Q(status__icontains=busca) | Q(cliente__nome__icontains=busca)| Q(veiculo__placa__icontains=busca) | Q(veiculo__marca_modelo__icontains=busca))
    todos = CadrastroServicos.objects.all().count()
    agendados = CadrastroServicos.objects.filter(status="Pendente").count()
    andamento = CadrastroServicos.objects.filter(status="Em andamento").count()
    concluidos = CadrastroServicos.objects.filter(status="Concluido").count()
    context = {'servicos': servicos, 'agendados': agendados, 'andamento': andamento, 'concluidos': concluidos, 'todos': todos, 'filtro': filtro}
    return render(request,'servicos/servicos.html', context)
@login_required
def cadastro_servico(request):
    if CadastroCliente.objects.count() == 0:
        messages.error(request, "Cadastre pelo menos um cliente antes de criar um serviço.")
        return redirect('clientes')

    if Veiculo.objects.count() == 0:
        messages.error(request, "Cadastre pelo menos um veículo antes de criar um serviço.")
        return redirect('veiculos')

    if request.method == 'POST':
        form = CadastroServicoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('servicos')
    else:
        form = CadastroServicoForm()
    return render(request, 'servicos/cadastro_servico.html', {'form': form})
@login_required
def detalhes_servico(request, id):
    objects = get_object_or_404(CadrastroServicos, pk=id)
    context = {'servico': objects}
    return render(request, 'servicos/detalhes_servico.html', context) 

class EditarServico(LoginRequiredMixin, UpdateView):
    model = CadrastroServicos
    form_class = CadastroServicoForm
    template_name = 'servicos/editar_servico.html'
    success_url = reverse_lazy('servicos')