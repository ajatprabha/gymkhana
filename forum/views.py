from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Topic
from .forms import TopicForm
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from hitcount.views import HitCountDetailView
from .mixins import UserAuthorMixin


class IndexView(LoginRequiredMixin, generic.ListView):
    model = Topic
    template_name = 'forum/index.html'
    context_object_name = 'topic_list'
    paginate_by = 15

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['range'] = range(context["paginator"].num_pages)
        return context


class TopicDetailView(LoginRequiredMixin, HitCountDetailView, generic.DetailView):
    model = Topic
    count_hit = True
    context_object_name = 'topic'
    template_name = 'forum/topic_detail.html'

    def get_context_data(self, **kwargs):
        """
        This has been overridden to add `answer_list` to the templates context,
        so you can use {% for answer in answer_list %} etc. within the template
        """
        context = super(TopicDetailView, self).get_context_data(**kwargs)
        context['answer_list'] = self.object.answer_set.all()
        return context


class TopicCreateView(LoginRequiredMixin, CreateView):
    form_class = TopicForm
    template_name = 'forum/topic_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user.userprofile
        return super(TopicCreateView, self).form_valid(form)


class TopicUpdateView(UserAuthorMixin, UpdateView):
    model = Topic
    form_class = TopicForm
    template_name = 'forum/topic_form_edit.html'


class TopicDeleteView(UserAuthorMixin, DeleteView):
    model = Topic
    success_url = reverse_lazy('forum:index')


@login_required
def test(request):
    return render(request, 'forum/test.html')
