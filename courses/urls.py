from django.urls import path, include
from . import views
from rest_framework import routers

# Create a router and register our viewset with it.
router = routers.DefaultRouter()
router.register("courses", views.CourseViewSet)

urlpatterns = [path("", include(router.urls))]
