from django.db import models

class Cliente(models.Model):
    nome = models.CharField('Nome', max_length=50, help_text='Nome do cliente')
    cpf = models.CharField('Cpf', max_length=11, help_text='CPF do Cliente', blank=True, null=True)
    cnpj = models.CharField('Cnpj', max_length=14, help_text='CPNJ do Cliente', blank=True, null=True)
    endereco = models.CharField('Endereco', max_length=50, help_text='Endereco do cliente')
    telefone = models.CharField('Telefone', max_length=11, help_text='Telefone do Cliente')
    email = models.EmailField('Email', max_length=50, help_text='Email do cliente')


    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'

    def __str__(self):
        return self.nome