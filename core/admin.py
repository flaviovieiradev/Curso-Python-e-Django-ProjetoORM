from django.contrib import admin

from .models import Chassi, Carro, Montadora


@admin.register(Montadora)
class MontadoraAdmin(admin.ModelAdmin):
    list_display = ('nome',)


@admin.register(Chassi)
class ChassiAdmin(admin.ModelAdmin):
    list_display = ('numero',)  # A vírgula é necessária, pois o list_display espera uma tupla.


@admin.register(Carro)
class CarroAdmin(admin.ModelAdmin):
    list_display = ('montadora', 'modelo', 'chassi', 'preco', 'get_motoristas')

    def get_motoristas(self, obj):
        return ', '.join([m.username for m in obj.motoristas.all()])
    
    get_motoristas.short_description = 'Motoristas'
