from django.contrib import admin
from .models import Society, Club, SocialLink


# iterable list
main_models = [
    Society,
    Club,
    SocialLink
]

admin.site.register(main_models)
