from django.contrib import admin

from .models import Cargo, Servico, Desenvolvedor

@admin.register(Cargo)
class CargoAdmin(admin.ModelAdmin):
    list_display = ('cargo', 'ativo', 'modificado')
 
@admin.register(Servico)   
class ServicoAdmin(admin.ModelAdmin):
    list_display = ('servico', 'icone', 'ativo', 'modificado')

@admin.register(Desenvolvedor)
class DesenvolvedorAdmin(admin.ModelAdmin):
    list_display = ('nome','cargo','modificado','ativo')

