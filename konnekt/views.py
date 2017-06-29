from oauth.models import UserProfile
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from django_searchbar.mixins import SearchBarViewMixin


class SearchView(LoginRequiredMixin, SearchBarViewMixin, ListView):
    model = UserProfile
    template_name = 'konnekt/index.html'
    searchbar_fields = ['skills']
    searchbar_method = 'get'
    searchbar_choices = (
        ('skills', 'Username'),
    )
    searchbar_replacements = {
        'skills': 'skills__icontains',
    }
