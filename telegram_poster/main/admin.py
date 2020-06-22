from django.contrib import admin
from main.models import Client, TelegramUser

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ['name', 'secret']

@admin.register(TelegramUser)
class TelegramUserAdmin(admin.ModelAdmin):
    list_display = ['key', 'client', 'name']