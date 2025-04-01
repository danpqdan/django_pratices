from django.db import models


class Cliente(models.Model):
    cpf = models.CharField(max_length=11, unique=True)
    nome = models.CharField(max_length=50)
    telefone = models.CharField(max_length=15)
    email = models.EmailField()

    def save(self, *args, **kwargs):
        self.cpf = "".join(filter(str.isdigit, self.cpf))
        super().save(*args, **kwargs)

    def __str__(self):
        return self.nome
