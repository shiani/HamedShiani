from django.http import Http404
from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import AllowAny
from .models import Resume
from . serializers import ResumeSerializer


class ResumeView(generics.RetrieveAPIView):
    serializer_class = ResumeSerializer
    permission_classes = (AllowAny,)

    def get_object(self):
        try:
            resume = Resume.objects.all().order_by('-create_date').first()
            return resume
        except Resume.DoesNotExist:
            raise Http404()
