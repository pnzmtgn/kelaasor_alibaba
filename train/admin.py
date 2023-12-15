from django.contrib.admin import ModelAdmin, register
from .models import Train, Station

@register(Train)
class FlightAdmin(ModelAdmin):
    autocomplete_fields = ["origin"]

@register(Station)
class StationAdmin(ModelAdmin):
    list_display = ["name", "city", "phone_number"]
    search_fields = ["name", "number"]
    list_filter = ["city"]

