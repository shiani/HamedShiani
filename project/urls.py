from django.urls import path
from project import views

app_name = "project"

urlpatterns = [
    path('project/list/', views.ProjectList.as_view(), name='project_list'),
]
