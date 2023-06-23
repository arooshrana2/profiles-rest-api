from django.urls import path

from profiles_api import views

urlpatterns = [
    path(route='hello-view/', view=views.HelloAPIView.as_view(), name='hello-api-view'),
]
