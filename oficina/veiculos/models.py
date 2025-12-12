from django.db import models
from clientes.models import CadastroCliente
from django.core.validators import MinValueValidator, MaxValueValidator
from datetime import datetime
# Create your models here.
# - placa
# - status (em andamento ou concluido)
# - marca/modelo
# - ano
# - cor
# - proprietario (estrangeira de cliente)
# - descrição

class Veiculo(models.Model):
    placa = models.CharField(max_length=8 , null=False, blank=False, unique=True)
    marca_modelo = models.CharField(max_length=100, null=False, blank=False)
    ano = models.IntegerField(
        validators=[
            MinValueValidator(1900),
            MaxValueValidator(datetime.now().year),
        ],
        null=False, blank=False)
    cor = models.CharField(max_length=100, null=False, blank=False)
    
    proprietario = models.ForeignKey('clientes.CadastroCliente', related_name='veiculos', on_delete=models.CASCADE)
    descricao = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.id} - {self.placa} - {self.marca_modelo}"
    # @classmethod
    # def quantidade_concluidos(cls):
    #     return cls.objects.filter(status='concluido').count()

    # @classmethod
    # def quantidade_em_andamento(cls):
    #     return cls.objects.filter(status='em_andamento').count()

    # @classmethod
    # def quantidade_agendados(cls):
    #     return cls.objects.filter(status='agendado').count()

    # @classmethod
    # def quantidade_esperando_pecas(cls):
    #     return cls.objects.filter(status='esperando_pecas').count()