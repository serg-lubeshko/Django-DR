from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy

from bboard.forms import BbForm
from bboard.models import Bb, Rubric
from django.views.generic.edit import CreateView


# def index(request):
#     s = "Список оъявлений: \r\n\r\n\r\n\r"
#
#     for item in Bb.objects.all():
#         s += item.title + '\r\n' + item.content + '\r\n\r\n'
#     return HttpResponse(s, content_type='text/plain; charset=utf-8')


def index(request):
    bbs = Bb.objects.all()
    rubrics = Rubric.objects.all()
    context = {'bbs': bbs, 'rubrics': rubrics}
    return render(request, template_name="bboard/index.html", context=context)


def by_rubric(request, rubric_id):
    bbs = Bb.objects.filter(rubric=rubric_id)
    rubrics = Rubric.objects.all()
    current_rubric = Rubric.objects.get(pk=rubric_id)
    context = {'bbs': bbs, 'rubrics': rubrics, 'current_rubric': current_rubric}
    return render(request, template_name='bboard/by_rubric.html', context=context)

class BbCreateView(CreateView):
    template_name = 'bboard/create.htm.html'
    form_class = BbForm
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['rubrics']  = Rubric.objects.all()
        return context


