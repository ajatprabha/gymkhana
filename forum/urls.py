from django.conf.urls import url
from forum import views
from django.contrib.auth.decorators import login_required

app_name = 'forum'

urlpatterns = [
    url(r'^$', login_required(views.IndexView.as_view()), name='index'),
    url(r'^topic/(?P<pk>[0-9])/$', login_required(views.TopicDetailView.as_view()), name='detail'),
    url(r'^topic/add/$', login_required(views.TopicCreateView.as_view()), name='add_topic'),
    url(r'^test/$', views.test, name='test'),
]