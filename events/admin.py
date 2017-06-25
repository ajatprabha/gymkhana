from django.contrib import admin
from .models import Event
# Register your models here.
event_models = [
    Event
]

admin.site.register(event_models)
