from django.urls import include, path
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register(r"shorten", views.ShortLinkViewSet, basename="shortify")
urlpatterns = [
    path("", include(router.urls)),
]
