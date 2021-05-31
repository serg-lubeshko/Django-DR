from django.urls import path, include

from .views import *

urlpatterns = [
    path('', index),
    path("<int:rubric_id>", by_rubric)
]