from django.http import Http404
from django.shortcuts import render
from rest_framework.permissions import AllowAny

from .models import ContactDetails
from .serializers import ContactFormSerializer, ContactDetailsSerializer
from rest_framework import generics


class ContactFormCreateView(generics.CreateAPIView):
    serializer_class = ContactFormSerializer
    permission_classes = (AllowAny,)


class ContactDetailsView(generics.RetrieveAPIView):
    serializer_class = ContactDetailsSerializer
    permission_classes = (AllowAny,)

    def get_object(self):
        try:
            contact_detail = ContactDetails.objects.first()
            return contact_detail
        except ContactDetails.DoesNotExist:
            raise Http404()