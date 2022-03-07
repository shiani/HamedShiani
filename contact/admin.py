from django.contrib import admin
from .models import ContactDetails, ContactForm

admin.site.register(ContactForm)
admin.site.register(ContactDetails)
