from django.conf.urls import url
from .views import ProfileDetailView, ProfileEditView

app_name = 'oauth'

urlpatterns = [
    url(r'^(?P<pk>\d+)/detail$', ProfileDetailView.as_view(), name='detail'),
    url(r'^(?P<pk>\d+)/edit$', ProfileEditView.as_view(), name='edit'),
]
