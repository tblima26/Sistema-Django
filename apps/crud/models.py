from django.db import models

class Paciente(models.Model):
    codigo_paciente = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=150, null=False, blank=False)
    cpf = models.CharField(max_length=14, unique=True, null=False, blank=False)
    email = models.EmailField(max_length=254, unique=True, null=False, blank=False)
    telefone = models.CharField(max_length=15, null=True, blank=True)
    data_nascimento = models.DateField(null=False, blank=False)
    sintomas = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.nome} - CPF: {self.cpf}"