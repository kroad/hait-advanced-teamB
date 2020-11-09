from django.urls import path

from . import views

app_name = "apiv1"
urlpatterns = [
    # path("songs/", views.SongListAPIView.as_view()),
    path("predict/", views.MLAPIView.as_view()),
]