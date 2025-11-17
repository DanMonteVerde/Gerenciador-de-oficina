from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import CadastroCliente
from .forms import CadastroClienteForm
from django.contrib import messages

# Create your views here.
@login_required
def clientes(request):
    clientes = CadastroCliente.objects.all()
    return render(request, 'clientes/clientes.html', {'clientes': clientes})
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
    return render(request, 'clientes/cadastro.html', {'form': form})

@login_required
def excluir_cliente(request, id):
    cliente = CadastroCliente.objects.get(id=id)
    cliente.delete()
    return redirect('clientes')

#FALTA O EDITAR, PARTICULAMENTE A PREGUIÇA BATEU, GABRIEL DO FUTURO UM CONSELHO TENHA PACIENCIA.