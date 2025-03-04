from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('list', views.ProjectLlist.as_view(), name="project-list"),
    path('detail/<slug>', views.ProjectDetail.as_view(), name="project-detail"),
]