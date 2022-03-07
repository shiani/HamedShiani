from django.urls import path
from project import views

app_name = "project"

urlpatterns = [
    path('project/list/', views.ProjectList.as_view(), name='project_list'),
    path('project/<slug:slug>/', views.ProjectSingle.as_view(), name='project_single'),
    path('project/tool/<slug:slug>/', views.ToolsList.as_view(), name='tool_list'),
    path('project/category/<slug:slug>/', views.CategoryList.as_view(), name='category_list'),
]
