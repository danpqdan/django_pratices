from django.db import models

class Produto(models.Model):
    codigo = models.CharField(max_length=13, unique=True)
    descricao = models.CharField(max_length=100)
    marca = models.CharField(max_length=30)
    quantidade_minima = models.DecimalField(max_digits=10, decimal_places=2)
    quantidade = models.DecimalField(max_digits=10, decimal_places=2)
    custo = models.DecimalField(max_digits=10, decimal_places=2)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    observacao = models.TextField(max_length=255, blank=True)

    def __str__(self):
        return self.descricao
