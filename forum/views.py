from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Topic, Answer
from .forms import TopicForm
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


class IndexView(LoginRequiredMixin, generic.ListView):
    template_name = 'index.html'
    context_object_name = 'topic_list'

    def get_queryset(self):
        return Topic.objects.all()


class TopicDetailView(LoginRequiredMixin, generic.DetailView):
    model = Topic
    context_object_name = 'topic_list'
    template_name = 'topicdetail.html'

    def get_context_data(self, **kwargs):
        """
        This has been overridden to add `topic` to the templates context,
        so you can use {{ topic }} etc. within the template
        """
        context = super(TopicDetailView, self).get_context_data(**kwargs)
        context['answer_list'] = self.object.answer_set.all()
        return context


class TopicCreateView(LoginRequiredMixin, CreateView):
    model = Topic
    form_class = TopicForm
    template_name = 'topic_form.html'


@login_required
def test(request):
    return render(request, 'test.html')
