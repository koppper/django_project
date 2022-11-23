from django.urls import path, re_path
from .views import animals

urlpatterns = [
    path('', animals),
]

