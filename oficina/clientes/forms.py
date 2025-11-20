from django import forms
from .models import CadastroCliente

class CadastroClienteForm(forms.ModelForm):
    class Meta:
        model = CadastroCliente
        fields = ['nome', 'email', 'telefone', 'endereco', 'cpf']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control', 'style': ''}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'telefone': forms.TextInput(attrs={'class': 'form-control'}),
            'endereco': forms.TextInput(attrs={'class': 'form-control'}),
            'cpf': forms.TextInput(attrs={'class': 'form-control'}),
        }