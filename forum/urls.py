from django.conf.urls import url
from forum import views
from django.contrib.auth.decorators import login_required

app_name = 'forum'

urlpatterns = [
    url(r'^$', login_required(views.IndexView.as_view()), name='index'),
    url(r'^test/$', views.test, name='test'),
]