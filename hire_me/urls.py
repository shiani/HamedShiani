from django.urls import path
from .views import HireMeView, HireMeSubjectList

app_name = "hire_me"


urlpatterns = [
    path("hire_me/subject_list/", HireMeSubjectList.as_view(), name="hire_me_subject_list"),
    path("hire_me/form/", HireMeView.as_view(), name="hire_me_form")
]