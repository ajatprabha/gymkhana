from django.views.generic import DetailView
from .models import UserProfile


class ProfileDetailView(DetailView):
    model = UserProfile
    template_name = 'oauth/profile_detail.html'
