from django.contrib import admin
from .models import CityData

class CityDataAdmin(admin.ModelAdmin):
    list_display = ('city_name', 'aqi_text', 'aqi_value', 'temperature', 'humidity', 'created_at')

admin.site.register(CityData, CityDataAdmin)
