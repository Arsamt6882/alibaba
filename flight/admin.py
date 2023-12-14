from django.contrib.admin import register,ModelAdmin
from .models import Flight, Airport

@register(Flight)
class FlightAdmin(ModelAdmin):
    pass


@register(Airport)
class AirportAdmin(ModelAdmin):
    pass

