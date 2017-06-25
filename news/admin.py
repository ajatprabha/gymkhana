from django.contrib import admin
from .models import News, Update

# Register your models here.
news_models = [
    News,
    Update
]

admin.site.register(news_models)
