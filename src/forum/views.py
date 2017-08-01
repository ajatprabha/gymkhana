from django.views.generic import CreateView, UpdateView, DeleteView, ListView, DetailView, FormView, View
from django.views.generic.detail import SingleObjectMixin
from .models import Topic
from .forms import TopicForm, AnswerForm
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from hitcount.views import HitCountDetailView
from .mixins import UserAuthorMixin


class IndexView(LoginRequiredMixin, ListView):
    model = Topic
    template_name = 'forum/index.html'
    context_object_name = 'topic_list'
    paginate_by = 15

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['range'] = range(context["paginator"].num_pages)
        return context


class TopicDisplay(HitCountDetailView, DetailView):
    count_hit = True
    model = Topic
    context_object_name = 'topic'
    template_name = 'forum/topic_detail.html'

    def get_context_data(self, **kwargs):
        context = super(TopicDisplay, self).get_context_data(**kwargs)
        context['answer_list'] = self.object.answer_set.all()
        context['form'] = AnswerForm()
        return context


class TopicAnswer(LoginRequiredMixin, SingleObjectMixin, FormView):
    template_name = 'forum/topic_detail.html'
    form_class = AnswerForm
    model = Topic

    def get_context_data(self, **kwargs):
        context = super(TopicAnswer, self).get_context_data(**kwargs)
        context['answer_list'] = self.object.answer_set.all()
        return context

    def form_valid(self, form):
        form.save()
        return super(TopicAnswer, self).form_valid(form)

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super(TopicAnswer, self).post(request, *args, **kwargs)

    def get_success_url(self):
        return self.object.get_absolute_url()


class TopicDetailView(LoginRequiredMixin, HitCountDetailView, View):

    def get(self, request, *args, **kwargs):
        view = TopicDisplay.as_view()
        return view(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        view = TopicAnswer.as_view()
        return view(request, *args, **kwargs)


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
