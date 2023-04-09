from django.db import models
from django.contrib.auth.models import User

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
    class Meta:
        verbose_name_plural = 'Autores'
    nome = models.CharField(max_length=255, blank=False, null=False)

    def __str__(self):
        return self.nome
    
class Livro(models.Model):
    titulo = models.CharField(max_length=300, blank=False, null=False)
    ISBN = models.CharField(max_length=40, blank=False, null=False)
    quantidade = models.IntegerField()
    preco = models.FloatField()
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT, related_name='livros') # se tentar fazer o delete de uma categoria, e tiver algum livro cadastrado nessa categoria, não será possível a exclusão. o related_name nós conseguimos fazer uma relação virtual para saber todos os livros que são de determinada categoria.
    editora = models.ForeignKey(Editora, on_delete=models.PROTECT, related_name='livros')
    autores = models.ManyToManyField(Autor, related_name='livros')

    def __str__(self):
        return "%s (%s)" %(self.titulo, self.editora)
    

class Compra(models.Model):

    class StatusCompra(models.IntegerChoices):
        CARRINHO = 1, 'Carrinho'
        REALIZADO = 2, 'Realizado'
        PAGO = 3, 'Pago'
        ENTREGUE = 4, 'Entregue'


    usuario = models.ForeignKey(User, on_delete=models.PROTECT, related_name='compras')
    status = models.IntegerField(choices=StatusCompra.choices, default=StatusCompra.CARRINHO)

class ItensCompra(models.Model):
    compra = models.ForeignKey(Compra, on_delete=models.CASCADE, related_name='itens')
    livro = models.ForeignKey(Livro, on_delete=models.PROTECT, related_name='+')
    quantidade = models.IntegerField()