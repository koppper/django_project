from django.urls import path
from .views import index, skylearn, post_z

urlpatterns = [
    path('', index),
    path('skylearn/', skylearn),
    path('post_z/', post_z)
]
