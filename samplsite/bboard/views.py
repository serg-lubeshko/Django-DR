from django.shortcuts import render


# Create your views here.
from bboard.models import Bb


def index(request):
    s= "Список оъявлений: \r\n\r\n\r\n\r"

    for item in Bb.objects.all:
        s += s

