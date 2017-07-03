from django.utils import timezone
from django.views.generic import TemplateView, DetailView
from .models import Society, Club, Senate, Festival
from events.models import Event
from news.models import News


class HomeView(TemplateView):
    template_name = 'main/index.html'

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        societies = Society.objects.filter(is_active=True)
        festivals = Festival.objects.all()[:4]
        context['society_link_list'] = societies
        context['festival_list'] = festivals
        return context


class SocietyView(DetailView):
    template_name = 'main/society.html'
    model = Society

    def get_context_data(self, **kwargs):
        context = super(SocietyView, self).get_context_data(**kwargs)
        societies = Society.objects.filter(is_active=True)
        raw = self.object.club_set.filter(published=True)
        clubs = raw.filter(ctype='C')
        teams = raw.filter(ctype='T')
        events = Event.objects.filter(club__society=self.object).filter(published=True).filter(
            date__gte=timezone.now())[:5]
        news = News.objects.filter(club__society=self.object).order_by('date')[:5]
        context['society_link_list'] = societies
        context['club_list'] = clubs
        context['team_list'] = teams
        context['event_list'] = events
        context['news_list'] = news
        return context


class SenateView(DetailView):
    template_name = 'main/senate.html'
    model = Senate

    def get_context_data(self, **kwargs):
        context = super(SenateView, self).get_context_data(**kwargs)
        societies = Society.objects.filter(is_active=True)
        context['society_link_list'] = societies
        return context


class ClubView(DetailView):
    template_name = 'main/club.html'
    model = Club

    def get_context_data(self, **kwargs):
        context = super(ClubView, self).get_context_data(**kwargs)
        society = Society.objects.filter(is_active=True)
        events = Event.objects.filter(club=self.object).filter(published=True)[:5]
        context['society_link_list'] = society
        context['event_list'] = events
        return context
