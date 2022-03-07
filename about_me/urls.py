from django.urls import path
from about_me import views

app_name = 'about_me'

urlpatterns = [
    path('about_me/', views.AboutMeSingle.as_view(), name='about_me')
]
