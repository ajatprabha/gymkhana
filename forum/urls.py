from django.conf.urls import url
from forum import views

app_name = 'forum'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^test/$', views.test, name='test'),
]