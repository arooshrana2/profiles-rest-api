from django.urls import path, include
from rest_framework.routers import DefaultRouter

from profiles_api import views

router = DefaultRouter()

router.register('hello-viewset-check', viewset=views.HelloViewSet, basename='hello-viewset')

urlpatterns = [
    path(route='hello-view/', view=views.HelloAPIView.as_view(), name='hello-api-view'),
    path('viewset/', include(router.urls))
]
