from django.db import models


class Editora(models.Model):
    nome = models.CharField(max_length=100, null=False, blank=False)
    site = models.URLField(null=True, blank=True)
    email = models.EmailField(max_length=100, blank=True, null=True)
    cidade = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f'({self.id}) {self.nome} '
