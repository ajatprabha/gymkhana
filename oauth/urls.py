from django.conf.urls import url
from .views import ProfileDetailView, ProfileEditView, SocialLinkCreateView, SocialLinkUpdateView, SocialLinkDeleteView

app_name = 'oauth'

urlpatterns = [
    url(r'^(?P<pk>\d+)/detail$', ProfileDetailView.as_view(), name='detail'),
    url(r'^(?P<pk>\d+)/edit$', ProfileEditView.as_view(), name='edit'),
    url(r'^sociallink/add$', SocialLinkCreateView.as_view(), name='link-add'),
    url(r'sociallink/(?P<username>[\w-]+)-(?P<social_media>[\w]{2})$', SocialLinkUpdateView.as_view(),
        name='link-edit'),
    url(r'sociallink/(?P<username>[\w-]+)-(?P<social_media>[\w]{2})/delete$', SocialLinkDeleteView.as_view(),
        name='link-delete'),
]
