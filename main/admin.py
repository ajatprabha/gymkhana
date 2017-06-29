from django.contrib import admin
from .models import Society, Club, SocialLink


class SocietyAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name", "year")}
    list_display = ('name', 'is_active', 'year')
    list_filter = ('year', 'is_active')


class ClubAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    list_display = ('__str__', 'society', 'ctype', 'published',)
    list_filter = ('published', 'ctype')

# iterable list
main_models = [
    SocialLink
]

admin.site.register(Society, SocietyAdmin)
admin.site.register(Club, ClubAdmin)
admin.site.register(main_models)
