from django.contrib import admin
from .models import User, Level, Tasks, Social_Network, EnergyLevel,  TapLevel, Card
from django.utils.safestring import mark_safe

class EnergyDisplay(admin.ModelAdmin):
    list_display = ('energy_level', 'price')

class TapDisplay(admin.ModelAdmin):
    list_display = ('tap_level', 'price')

class LevelDisplay(admin.ModelAdmin):
    search_fields  = ("title", )
    list_display = ('title', 'level', 'min_balance', 'max_balance')

class TaskDisplay(admin.ModelAdmin):
    search_fields = ("title", "url",)
    list_display = ("title", "url", "social_network", "earn")

class UserDisplay(admin.ModelAdmin):
    search_fields = ('chat_id', 
        'username', 
        'first_name', 
        'last_name',
        'balance',
        'energy',)
    
    list_display = ('chat_id', 
        'username', 
        'first_name', 
        'last_name',
        'balance',
        'energy',
        )

class CardDisplay(admin.ModelAdmin):

    list_display = ('title', 'price', 'earn_per_hour', 'category')

admin.site.register(User, UserDisplay)
admin.site.register(Level, LevelDisplay)
admin.site.register(Tasks, TaskDisplay)
admin.site.register(Social_Network)
admin.site.register(EnergyLevel, EnergyDisplay)
admin.site.register(TapLevel, TapDisplay)
admin.site.register(Card, CardDisplay)