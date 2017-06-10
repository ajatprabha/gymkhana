from django.views import generic
from .models import Topic
from django.shortcuts import render
from django.contrib.auth.decorators import login_required


class IndexView(generic.ListView):
    template_name = 'index.html'
    context_object_name = 'topic_list'

    def get_queryset(self):
        return Topic.objects.all()


@login_required
def test(request):
    return render(request, 'test.html')
