from oauth.models import UserProfile
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, TemplateView
from django_searchbar.mixins import SearchBarViewMixin


class HomeView(TemplateView):
    template_name = 'konnekt/index.html'


class SearchView(LoginRequiredMixin, SearchBarViewMixin, ListView):
    model = UserProfile
    template_name = 'konnekt/search.html'
    searchbar_fields = ['skills']
    searchbar_method = 'get'
    searchbar_choices = (
        ('skills', 'Username'),
    )
    searchbar_replacements = {
        'skills': 'skills__icontains',
    }
