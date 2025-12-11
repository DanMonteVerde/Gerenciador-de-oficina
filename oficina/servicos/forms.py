from django import forms
from .models import CadrastroServicos
#ISSO FOI CHAT somente pra data na ediçao nao ficar vazia
class CadastroServicoForm(forms.ModelForm):
    class Meta:
        model = CadrastroServicos
        fields = '__all__'
        widgets = {
            'data_agendamento': forms.DateInput(
                attrs={'type': 'date'},
                format='%Y-%m-%d'
            )
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Faz o Django exibir a data já salva
        if self.instance and self.instance.pk:
            self.fields['data_agendamento'].initial = self.instance.data_agendamento