from django.contrib import admin
from .models import Cliente, Produto
# Register your models here.

class ClienteAdmin(admin.ModelAdmin):
    list_display=('nome', 'sobrenome', 'email')
    search_fields=('nome', 'sobrenome', 'email')
    list_filter=('nome', 'sobrenome', 'email')
class ProdutoAdmin(admin.ModelAdmin):
    list_display=('nome', 'preco', 'estoque')
    search_fields=('nome', 'preco', 'estoque')
    list_filter=('nome',)

admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Produto, ProdutoAdmin)
