from django.contrib import admin
from .models import Topic, Answer, Reply


class TopicAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_at'
    list_display = ('title', 'author', 'created_at')
    list_filter = ('created_at',)

    class Meta:
        model = Topic

admin.site.register(Topic, TopicAdmin)


class AnswerAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_at'
    list_display = ('topic', 'author', 'created_at')
    list_filter = ('created_at',)

    class Meta:
        model = Answer

admin.site.register(Answer, AnswerAdmin)


class ReplyAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_at'
    list_display = ('answer', 'author', 'created_at')
    list_filter = ('created_at',)

    class Meta:
        model = Reply

admin.site.register(Reply, ReplyAdmin)
