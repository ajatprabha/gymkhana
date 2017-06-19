from django.conf.urls import url
from . import views

app_name = 'forum_api'

urlpatterns = [
    url(r'^topic/$', views.TopicListAPIView.as_view(), name='topic-list'),
    # url(r'^topic/(?P<pk>\d+)/$', views.TopicDetailView.as_view(), name='detail'),
    # url(r'^topic/add/$', views.TopicCreateView.as_view(), name='add_topic'),
    # url(r'^topic/(?P<pk>\d+)/update/$', views.TopicUpdateView.as_view(), name='update_topic'),
    # url(r'^topic/(?P<pk>\d+)/delete/$', views.TopicDeleteView.as_view(), name='delete_topic'),
    # url(r'^test/$', views.test, name='test'),
]