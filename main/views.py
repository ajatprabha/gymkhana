from django.views.generic import TemplateView, DetailView
from .models import Society, Club


class HomeView(TemplateView):
    template_name = 'main/index.html'


class ClubView(DetailView):
    template_name = 'main/base.html'
    model = Club


class SocietyView(DetailView):
    template_name = 'main/index.html'
    model = Society
