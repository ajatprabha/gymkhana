from rest_framework.serializers import ModelSerializer
from forum.models import Topic


class TopicSerializer(ModelSerializer):
    class Meta:
        model = Topic
        fields = [
            'id',
            'title',
            'author',
            'category',
            'created_at',
        ]