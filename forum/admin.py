from django.contrib import admin
from .models import Topic, Answer, Tag


# iterable list
forum_models = [
    Topic,
    Answer,
    Tag
]

admin.site.register(forum_models)
