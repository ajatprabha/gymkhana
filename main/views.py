from django.views.generic import TemplateView, DetailView
from .models import Society, Club
from django.shortcuts import render_to_response


class HomeView(TemplateView):
    template_name = 'main/index.html'

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        society = Society.objects.filter(is_active=True)
        context['society_link_list'] = society
        return context


class SocietyView(DetailView):
    template_name = 'main/society.html'
    model = Society

    def get_context_data(self, **kwargs):
        context = super(SocietyView, self).get_context_data(**kwargs)
        society = Society.objects.filter(is_active=True)
        clubs = self.object.club_set.all()
        context['society_link_list'] = society
        context['club_list'] = clubs
        return context


class ClubView(DetailView):
    template_name = 'main/club.html'
    model = Club

    def get_context_data(self, **kwargs):
        context = super(ClubView, self).get_context_data(**kwargs)
        society = Society.objects.filter(is_active=True)
        context['society_link_list'] = society
        return context
