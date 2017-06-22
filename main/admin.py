from django.contrib import admin
from .models import Society, Club, SocialLink


class SocietyAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name", "year")}


class ClubAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}

# iterable list
main_models = [
    SocialLink
]

admin.site.register(Society, SocietyAdmin)
admin.site.register(Club, ClubAdmin)
admin.site.register(main_models)
