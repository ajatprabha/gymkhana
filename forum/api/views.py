from rest_framework.generics import ListAPIView
from forum.models import Topic
from .serializers import TopicSerializer


class TopicListAPIView(ListAPIView):
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer
