from django.conf.urls import url
from .views import ProfileDetailView

app_name = 'oauth'

urlpatterns = [
    url(r'^(?P<pk>\d+)/detail$', ProfileDetailView.as_view(), name='detail'),
]
