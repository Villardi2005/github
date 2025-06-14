from django.contrib import admin
from .models import Professor,Usuario,Responsavel

@admin.register(Professor)
class ProfessorAdmin(admin.ModelAdmin):
    list_display = ['nome', 'email']
    search_fields = ['nome', 'email']

@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'nome_completo', 'telefone']

admin.site.register(Responsavel)
