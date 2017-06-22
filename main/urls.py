from django.conf.urls import url
from .views import HomeView, SocietyView, ClubView, dynamic_css

app_name = 'main'

urlpatterns = [
    url(r'^$', HomeView.as_view(), name='index'),
    url(r'^society/(?P<slug>[\w-]+)', SocietyView.as_view(), name='soc-detail'),
    url(r'^society-css/(?P<id>\d+)/dynamic.css$', dynamic_css, name='dyn-css'),
    url(r'^club/(?P<slug>[\w-]+)', ClubView.as_view(), name='club-detail'),
]
