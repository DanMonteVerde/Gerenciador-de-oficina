from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import CadastroCliente
from .forms import CadastroClienteForm
from django.contrib import messages
from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy
from django.db.models import Q
# Create your views here.
@login_required
def clientes(request):
    busca = request.GET.get('q', '')
    clientes = CadastroCliente.objects.all()
    if busca:
        clientes = clientes.filter(
            Q(nome__icontains=busca)|
            Q(telefone__icontains=busca)|
            Q(endereco__icontains=busca)|
            Q(email__icontains=busca)
        )
    return render(request, 'clientes/clientes.html', {'clientes': clientes, 'busca': busca})
@login_required
def cadastro(request):
    if request.method == 'POST':
        form = CadastroClienteForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Cliente cadastrado com sucesso!")
            return redirect('clientes')
    else:
        form = CadastroClienteForm()    
    return render(request, 'clientes/cadastro_cliente.html', {'form': form})

@login_required
def excluir_cliente(request, id):
    cliente = CadastroCliente.objects.get(id=id)
    cliente.delete()
    return redirect('clientes')

#FALTA O EDITAR, PARTICULAMENTE A PREGUIÇA BATEU, GABRIEL DO FUTURO UM CONSELHO TENHA PACIENCIA.
class EditarCliente(UpdateView):
    model = CadastroCliente
    form_class = CadastroClienteForm
    template_name = 'clientes/editar_clientes.html'
    success_url = reverse_lazy('clientes')