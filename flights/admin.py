from django.contrib.admin import ModelAdmin, register
from .models import Flight, Airport

@register(Flight)
class FlightAdmin(ModelAdmin):
    autocomplete_fields = ["origin"]

@register(Airport)
class AirportAdmin(ModelAdmin):
    list_display = ["name", "No", "city", "phone_number"]
    search_fields = ["name", "number"]
    list_filter = ["city"]

