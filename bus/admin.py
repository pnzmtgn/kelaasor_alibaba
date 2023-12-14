from django.contrib.admin import ModelAdmin, register
from .models import Bus, Terminal

@register(Bus)
class BusAdmin(ModelAdmin):
    pass

@register(Terminal)
class TerminalAdmin(ModelAdmin):
    pass

