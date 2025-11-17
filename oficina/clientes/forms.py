from django import forms
from .models import CadastroCliente

class CadastroClienteForm(forms.ModelForm):
    class Meta:
        model = CadastroCliente
        fields = ['nome', 'email', 'telefone', 'endereco']