from django import forms
from .models import CadrastroServicos
from clientes.models import CadastroCliente
from veiculos.models import Veiculo
from django.core.exceptions import ValidationError
#ISSO FOI CHAT somente pra data na ediçao nao ficar vazia
class CadastroServicoForm(forms.ModelForm):
    cliente = forms.ModelChoiceField(queryset=CadastroCliente.objects.all(), required=True, label= "Cliente")
    class Meta:
        model = CadrastroServicos
        fields = ['cliente',
            'veiculo',
            'tipo',
            'mecanico',
            'data_agendamento',
            'valor',
            'status',
            'descricao',
            'prioridade']
        widgets = {
            'data_agendamento': forms.DateInput(
                attrs={'type': 'date'},
                format='%Y-%m-%d'
            )
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # (UPDATE)
        if self.instance and self.instance.pk:
            self.fields['data_agendamento'].initial = self.instance.data_agendamento

            veiculo = self.instance.veiculo
            proprietario = veiculo.proprietario

            self.fields['cliente'].initial = proprietario
            self.fields['veiculo'].queryset = Veiculo.objects.filter(
                proprietario=proprietario
            )

        #  (POST)
        elif 'cliente' in self.data:
            try:
                cliente_id = int(self.data.get('cliente'))
                self.fields['veiculo'].queryset = Veiculo.objects.filter(
                    proprietario_id=cliente_id
                )
            except (ValueError, TypeError):
                self.fields['veiculo'].queryset = Veiculo.objects.none()

        #  (GET)
        else:
            self.fields['veiculo'].queryset = Veiculo.objects.none()
    def clean(self):
        cleaned_data = super().clean()

        cliente = cleaned_data.get('cliente')
        veiculo = cleaned_data.get('veiculo')

        if cliente and veiculo:
            if veiculo.proprietario != cliente:
                raise ValidationError(
                    "O veículo selecionado não pertence ao cliente escolhido."
                )

        return cleaned_data