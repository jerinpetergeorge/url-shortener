from django.urls import path

from .. import views

urlpatterns = [
    path("<str:code>/", views.RedirectView.as_view(), name="redirect"),
]
