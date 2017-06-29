from django.contrib import admin
from .models import News, Update


class NewsAdmin(admin.ModelAdmin):
    date_hierarchy = 'date'
    list_display = ('title', 'author', 'club', 'date')
    list_filter = ('date',)

    class Meta:
        model = News


class UpdateAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_at'
    list_display = ('title', 'created_at')
    list_filter = ('created_at',)

    class Meta:
        model = Update


admin.site.register(News, NewsAdmin)
admin.site.register(Update, UpdateAdmin)
