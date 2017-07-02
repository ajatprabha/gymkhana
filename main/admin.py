from django.contrib import admin
from .models import Society, Club, SocialLink, Senate, SenateMembership


class MembershipInline(admin.StackedInline):
    model = SenateMembership
    can_delete = True
    verbose_name_plural = 'Members'


class SenateAdmin(admin.ModelAdmin):
    inlines = (MembershipInline,)


class SocietyAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name", "year")}
    list_display = ('name', 'is_active', 'year')
    list_filter = ('year', 'is_active')


class ClubAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    list_display = ('__str__', 'society', 'ctype', 'published')
    list_filter = ('published', 'ctype')

# iterable list
main_models = [
    SocialLink,
]

admin.site.register(Society, SocietyAdmin)
admin.site.register(Club, ClubAdmin)
admin.site.register(Senate, SenateAdmin)
admin.site.register(main_models)
