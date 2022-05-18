from . import views
from django.urls import path, include
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("hello-viewset", views.HelloViewSet, basename="hello-viewset")
router.register('profile', views.UserProfileViewSet) #UserProfileViewSet has query set then we dont need to basename

urlpatterns = [
    path("hello-view/", views.HelloAPIView.as_view()),
    path("", include(router.urls)),
]
