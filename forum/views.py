from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Topic, Answer
from django.shortcuts import render
from django.contrib.auth.decorators import login_required


class IndexView(generic.ListView):
    template_name = 'index.html'
    context_object_name = 'topic_list'

    def get_queryset(self):
        return Topic.objects.all()


class TopicDetailView(generic.DetailView):
    model = Topic
    context_object_name = 'topic'
    template_name = 'topicdetail.html'

    def get_context_data(self, **kwargs):
        """
        This has been overridden to add `answer` to the templates context,
        so you can use {{ answer }} etc. within the template
        """
        context = super(TopicDetailView, self).get_context_data(**kwargs)
        context["answer"] = Answer.objects.all()
        return context


class TopicCreateView(CreateView):
    model = Topic
    fields = ['category', 'title', 'content', 'tags']


@login_required
def test(request):
    return render(request, 'test.html')
