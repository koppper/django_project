from django.urls import path, re_path
from .views import animals, people

urlpatterns = [
    path('', animals),
    path("peoples/", people)
]

