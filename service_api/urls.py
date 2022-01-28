from django.urls import path

from . import views


urlpatterns = [
    path("external-fake-api/", views.ExternalFakeApi.as_view()),
]
