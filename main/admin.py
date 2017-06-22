from django.contrib import admin
from .models import Society, Club, SocialLink


class SocietyAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}

# iterable list
main_models = [
    Club,
    SocialLink
]

admin.site.register(Society, SocietyAdmin)
admin.site.register(main_models)
