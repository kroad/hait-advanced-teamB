from django.urls import path

from . import views

app_name = "apiv1"
urlpatterns = [
    path("predict/", views.MLAPIView.as_view()),
    path("test/", views.TestAPIView.as_view()),
]