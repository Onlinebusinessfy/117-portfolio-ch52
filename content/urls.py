from django.urls import path
from . import views

urlpatterns=[
    path("", views.ProjectsListView.as_view(), name="project_list"),
    path("new_project/", views.project_new_view, name="project_new"),
]