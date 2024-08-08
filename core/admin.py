from django.contrib import admin

from .models import Chassi, Carro


@admin.register(Chassi)
class ChassiAdmin(admin.ModelAdmin):
    list_display = ('numero',)  # A vírgula é necessária, pois o list_display espera uma tupla.


@admin.register(Carro)
class CarroAdmin(admin.ModelAdmin):
    list_display = ('modelo', 'chassi', 'preco')
