from django.conf.urls import url
from .views import HomeView, SocietyView, ClubView, SenateView, ActivityView

app_name = 'main'

urlpatterns = [
    url(r'^$', HomeView.as_view(), name='index'),
    url(r'^society/(?P<slug>[\w-]+)', SocietyView.as_view(), name='soc-detail'),
    url(r'^senate/(?P<slug>[\w-]+)', SenateView.as_view(), name='senate-detail'),
    url(r'^club/(?P<slug>[\w-]+)', ClubView.as_view(), name='club-detail'),
    url(r'^activity-club/(?P<pk>\d+)', ActivityView.as_view(), name='activity-gallery'),
]
