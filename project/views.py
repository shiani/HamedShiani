from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import AllowAny

from .models import Project
from .seializers import ProjectSerializer


class ProjectList(generics.ListAPIView):
    serializer_class = ProjectSerializer
    permission_classes = (AllowAny,)

    def get_queryset(self):
        return Project.objects.filter(is_active=True)