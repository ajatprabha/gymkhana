from django.contrib import admin
from .models import Event, GeneralEvent

# Register your models here.
event_models = [
    Event,
    GeneralEvent
]

admin.site.register(event_models)
