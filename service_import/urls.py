from django.urls import path

from . import views


urlpatterns = [
    path("run-import-task/", views.RunImportTask.as_view()),
]
