from django.http import Http404
from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import AllowAny

from .models import AboutMe
from .serializers import AboutMeSerializer


class AboutMeSingle(generics.RetrieveAPIView):
    serializer_class = AboutMeSerializer
    permission_classes = (AllowAny,)

    def get_object(self):
        try:
            about = AboutMe.objects.first()
            return about
        except AboutMe.DoesNotExist:
            raise Http404()

