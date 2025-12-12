from django.shortcuts import render, redirect
from .forms import VeiculoForm
from .models import Veiculo
from django.contrib import messages
from clientes.models import CadastroCliente
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import UpdateView
from django.contrib.auth.decorators import login_required
from django.db.models import Q

# Create your views here.
@login_required
def index(request):
    buscar = request.GET.get('q', '')
    if buscar:
        veiculos = Veiculo.objects.filter(
            Q(placa__icontains=buscar) |
            Q(marca_modelo__icontains=buscar) |
            Q(cor__icontains=buscar)
        )
    else:
        veiculos = Veiculo.objects.all()
    context = {'veiculos': veiculos, 'total_veiculos': Veiculo.objects.all().count(), 'total_veiculos_antigos': Veiculo.antigos(), 'total_veiculos_novos': Veiculo.novos_veiculos()}
    return render(request, 'veiculos/veiculos.html', context)
@login_required
def cadastro_veiculo(request):
    # TESTAR SE ESSE IF FUNCIONA DEPOIS
    if not CadastroCliente.objects.exists():
        messages.error(request, "Você precisa cadastrar um cliente antes de cadastrar um veículo.")
        return redirect('clientes')
    if request.method == 'POST':
        form = VeiculoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('veiculos')
    else:
        form = VeiculoForm()
    return render(request, 'veiculos/cadastro_veiculo.html', {'form': form})

#DEPOIS FAREI O DE DETALHES (NAO É OBRIGATORIO)
@login_required
def excluir_veiculo(request, id):
    veiculo = Veiculo.objects.get(id=id)
    veiculo.delete()
    return redirect('veiculos')

class VeiculoUpdateView(LoginRequiredMixin, UpdateView):
    model = Veiculo
    form_class = VeiculoForm
    template_name = 'veiculos/update_veiculo.html'
    success_url = '/veiculos'