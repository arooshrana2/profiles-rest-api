from django.urls import path, include
from rest_framework.routers import DefaultRouter

from profiles_api import views

router = DefaultRouter()

router.register('hello-viewset-check', viewset=views.HelloViewSet, basename='hello-viewset')
router.register('update-profile', viewset=views.UserProfileView)
router.register('feed', viewset=views.UserProfileFeedViewSet)


urlpatterns = [
    path(route='hello-view/', view=views.HelloAPIView.as_view(), name='hello-api-view'),
    path(route="login/", view=views.UserLoginAPIView.as_view(), name="login-api-view"),
    path('viewset/', include(router.urls))
]
