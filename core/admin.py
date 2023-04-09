from django.contrib import admin
from core.models import Autor, Categoria, Compra, Editora, ItensCompra, Livro

class Autores(admin.ModelAdmin):
    list_display = ('id', 'nome')
    list_display_links = ('id', 'nome')

admin.site.register(Autor, Autores)

class Categorias(admin.ModelAdmin):
    list_display = ('id', 'descricao')
    list_display_links = ('id', 'descricao')

admin.site.register(Categoria, Categorias)

class Editoras(admin.ModelAdmin):
    list_display = ('id', 'nome', 'site')
    list_display_links = ('id', 'nome')

admin.site.register(Editora, Editoras)

class Livros(admin.ModelAdmin):
    list_display = ('id', 'titulo', 'ISBN', 'quantidade', 'preco', 'categoria', 'editora')
    list_display_links = ('id', 'titulo', 'categoria', 'editora')
admin.site.register(Livro, Livros)

class ItensInline(admin.TabularInline):
    model = ItensCompra

@admin.register(Compra)
class Compras(admin.ModelAdmin):
    inlines = (ItensInline,)