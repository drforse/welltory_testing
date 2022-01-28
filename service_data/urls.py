from django.urls import path

from . import views


urlpatterns = [
    path("weight/", views.UserWeightView.as_view()),
    path("weights/", views.UserWeightsView.as_view())
]
