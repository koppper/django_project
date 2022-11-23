from django.urls import path
from django.views.generic import TemplateView

from .views import ext

urlpatterns = [
    path('', ext),
    # path('ext/', ext)
]

