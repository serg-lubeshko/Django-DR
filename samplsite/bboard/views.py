from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from bboard.models import Bb, Rubric


# def index(request):
#     s = "Список оъявлений: \r\n\r\n\r\n\r"
#
#     for item in Bb.objects.all():
#         s += item.title + '\r\n' + item.content + '\r\n\r\n'
#     return HttpResponse(s, content_type='text/plain; charset=utf-8')


def index(request):
    bbs = Bb.objects.all()
    context = {'bbs': bbs}
    return render(request, template_name="bboard/index.html", context=context)


def rubric_id(request, rubric_id):
    bbs = Bb.objects.filter(rubric=rubric_id)
    rubrics = Rubric.objects.all()
    current_rubric = Rubric.objects.get(pk=rubric_id)
    context = {'bbs':bbs,'rubrics':rubrics,'current_rubric':current_rubric}
    return render(request, template_name='bboard/index.html', context=context)
