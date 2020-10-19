from django.urls import path, include
from rest_framework import routers
from rest_framework import urlpatterns

from . import views

router= routers.DefaultRouter()
router.register('songs1', views.SongViewSet)

app_name = 'apiv1'
urlpatterns = [
    path('', include(router.urls)),
    path('songs2/', views.SongListAPIView.as_view()),
]