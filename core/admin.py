from django.contrib import admin
from .models import User, Level, Tasks, Social_Network, EnergyLevel

class EnergyDisplay(admin.ModelAdmin):
    list_display = ('energy_level', 'price')

class LevelDisplay(admin.ModelAdmin):
    search_fields  = ("title", )
    list_display = ('title', 'level', 'min_balance')

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

admin.site.register(User, UserDisplay)
admin.site.register(Level, LevelDisplay)
admin.site.register(Tasks, TaskDisplay)
admin.site.register(Social_Network)
admin.site.register(EnergyLevel, EnergyDisplay)