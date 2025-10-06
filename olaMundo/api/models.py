from django.db import models
# Create your models here.
class Cliente(models.Model):
    nome = models.CharField('Nome', max_length=100)
    sobrenome = models.CharField('sobrenome', max_length=100)
    email = models.CharField('E-mail', max_length=100)
    def __str__(self):
        return f'{self.nome} {self.sobrenome} | {self.email}'
    
class Produto(models.Model):
    nome = models.CharField('Nome', max_length=100)
    preco = models.DecimalField('Preco', decimal_places=2, max_digits=8)
    estoque = models.IntegerField('Quantidadode em Estoque')
    def __str__(self):
        return f'{self.nome}'     