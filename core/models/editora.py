from django.db import models


class Editora(models.Model):
    nome = models.CharField(max_length=100, null=False)
    site = models.URLField()

    def __str__(self):
        return f'{self.nome} {self.id}'
