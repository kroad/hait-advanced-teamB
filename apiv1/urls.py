from django.urls import path
from rest_framework import urlpatterns

from . import views

app_name = 'apiv1'
urlpatterns = [
    path('songs/', views.SongListAPIView.as_view()),
]