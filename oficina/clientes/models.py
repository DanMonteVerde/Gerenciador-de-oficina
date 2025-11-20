from django.db import models

# Create your models here.
class CadastroCliente(models.Model):
    nome = models.CharField(max_length=100, null=False, blank=False)
    email = models.EmailField(null = False, blank = True)
    telefone = models.CharField(max_length=20, null = False, blank = False)
    endereco = models.CharField(max_length=100, null=True, blank=True)
    cpf = models.CharField(max_length=11, null = True, blank = True, unique=True)
    def __str__(self):
        return f"{self.id} - {self.nome} - {self.email}"

    @property
    def quantidade_veiculos(self):
        return self.veiculos.count()