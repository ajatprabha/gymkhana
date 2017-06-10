from django.conf.urls import url
from forum import views

app_name = 'forum'

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^topic/(?P<pk>[0-9])/$', views.TopicDetailView.as_view(), name='detail'),
    url(r'^topic/add/$', views.TopicCreateView.as_view(), name='add_topic'),
    url(r'^test/$', views.test, name='test'),
]