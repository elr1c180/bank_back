from django.contrib import admin
from .models import User, Level, Tasks, Social_Network, EnergyLevel,  TapLevel, Card
from django.utils.safestring import mark_safe

class EnergyDisplay(admin.ModelAdmin):
    list_display = ('energy_level', 'price')

class TapDisplay(admin.ModelAdmin):
    list_display = ('tap_level', 'price')

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

class CardDisplay(admin.ModelAdmin):

    readonly_fields = ["preview"]

    def preview(self, obj):
        return mark_safe("<img width='50' src='https://upload.wikimedia.org/wikipedia/commons/thumb/9/95/Instagram_logo_2022.svg/1000px-Instagram_logo_2022.svg.png'>")

admin.site.register(User, UserDisplay)
admin.site.register(Level, LevelDisplay)
admin.site.register(Tasks, TaskDisplay)
admin.site.register(Social_Network)
admin.site.register(EnergyLevel, EnergyDisplay)
admin.site.register(TapLevel, TapDisplay)
admin.site.register(Card, CardDisplay)