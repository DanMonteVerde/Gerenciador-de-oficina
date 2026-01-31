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
        (1, "Pendente"),
        (2, "Em andamento"),
        (3, "Concluído"),
    ]
    PRIORIDADE = [
        (3, "Baixa"),
        (2, "Normal"),
        (1, "Alta"),
    ]
    tipo = models.CharField(max_length=50, choices=TIPOS_DE_SERVICOS)
    #CONVERSAR SOBRE CHAVE ESTRANGEIRA COM O PROFESSOR DEPOIS
    veiculo = models.ForeignKey(Veiculo, on_delete=models.CASCADE, null=True)
    mecanico = models.CharField(max_length=100, null=True, blank=True)
    data_agendamento = models.DateField(null=False, blank=False)
    valor = models.DecimalField(
        max_digits=20,
        decimal_places=2,    
        validators=[MinValueValidator(Decimal('0.00'))], 
        null = False,
        blank = False,
    )
    status = models.IntegerField(choices=STATUS, null=False, blank=False, default=1)
    descricao = models.TextField(null=True, blank=True)
    prioridade = models.IntegerField(choices=PRIORIDADE, null=False, blank=False, default=2)
    class Meta:
        ordering = ['prioridade', '-data_agendamento']
    def __str__(self):
        return str(self.id)
    @classmethod
    def quantidade_concluidos(cls):
        return cls.objects.filter(status=3).count()

    @classmethod
    def quantidade_pendentes(cls):
        return cls.objects.filter(status=1).count()

    @classmethod
    def quantidade_em_andamento(cls):
        return cls.objects.filter(status=2).count()