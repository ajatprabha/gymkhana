from django.views.generic import TemplateView, DetailView
from .models import Society, Club


class HomeView(TemplateView):
    template_name = 'main/index.html'

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        society = Society.objects.all()
        context['society_list'] = society
        return context


class SocietyView(DetailView):
    template_name = 'main/society.html'
    model = Society

    def get_context_data(self, **kwargs):
        context = super(SocietyView, self).get_context_data(**kwargs)
        society = Society.objects.all()
        context['society_list'] = society
        return context


class ClubView(DetailView):
    template_name = 'main/club.html'
    model = Club

    def get_context_data(self, **kwargs):
        context = super(ClubView, self).get_context_data(**kwargs)
        society = Society.objects.all()
        context['society_list'] = society
        return context
