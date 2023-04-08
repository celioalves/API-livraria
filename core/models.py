from django.db import models

class Categoria(models.Model):
    descricao = models.CharField(max_length=100, blank=False, null=False)

    def __str__(self):
        return self.descricao

class Editora(models.Model):
    nome = models.CharField(max_length=40, blank=False, null=False)
    site = models.URLField(blank=False, null=False)

    def __str__(self):
        return self.nome

class Autor(models.Model):
    nome = models.CharField(max_length=100, blank=False, null=False)

    def __str__(self):
        return self.nome