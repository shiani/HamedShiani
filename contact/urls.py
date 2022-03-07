from django.urls import path
from contact import views
app_name = 'contact'

urlpatterns = [
    path('contact/form/', views.ContactFormCreateView.as_view(), name='contact_form'),
    path('contact/details/', views.ContactDetailsView.as_view(), name='contact_details'),
]
