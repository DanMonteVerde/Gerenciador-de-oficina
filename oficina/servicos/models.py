from django.db import models
from veiculos.models import Veiculo
from clientes.models import CadastroCliente
from django.core.validators import MinValueValidator
from decimal import Decimal
# Create your models here.
class CadrastroServicos(models.Model):
    TIPOS_DE_SERVICOS = [
        ("Troca de óleo", "Troca de óleo"),
        ("Troca de filtros", "Troca de filtros"),
        ("Revisão", "Revisão"),
        ("Alinhamento e balanceamento", "Alinhamento e balanceamento"),
        ("Freios", "Freios"),
        ("Suspensão", "Suspensão"),
        ("Troca de pneus", "Troca de pneus"),
        ("Ar-condicionado", "Ar-condicionado"),
        ("Elétrica", "Elétrica"),
        ("Diagnóstico eletrônico", "Diagnóstico eletrônico"),
        ("Correias", "Correias"),
        ("Embreagem", "Embreagem"),
        ("Motor e câmbio", "Motor e câmbio"),
    ]

    STATUS = [
        ("Pendente", "Pendente"),
        ("Em andamento", "Em andamento"),
        ("Concluído", "Concluído"),
    ]
    PRIORIDADE = [
        ("Baixa", "Baixa"),
        ("Normal", "Normal"),
        ("Alta", "Alta"),
    ]
    tipo = models.CharField(max_length=50, choices=TIPOS_DE_SERVICOS)
    veiculo = models.ForeignKey(Veiculo, on_delete=models.SET_NULL, null=True)
    cliente = models.ForeignKey(CadastroCliente, on_delete=models.SET_NULL, null=True)
    mecanico = models.CharField(max_length=100, null=True, blank=True)
    data_agendamento = models.DateField(null=False, blank=False)
    valor = models.DecimalField(
        max_digits=20,
        decimal_places=2,    
        validators=[MinValueValidator(Decimal('0.00'))], 
        null = False,
        blank = False,
    )
    status = models.CharField(max_length=20, choices=STATUS, null=False, blank=False, default='Pendente')
    descricao = models.TextField(null=True, blank=True)
    prioridade = models.CharField(max_length=20, choices=PRIORIDADE, null=False, blank=False, default='Normal')
    def __str__(self):
        return str(self.id)