from django.shortcuts import render
from rest_framework.permissions import AllowAny
from .models import HireMe, HireMeSubject
from .serializers import HireMeSerializer, HireMeSubjectSerializer
from rest_framework import generics


class HireMeSubjectList(generics.ListAPIView):
    serializer_class = HireMeSubjectSerializer
    permission_classes = (AllowAny,)
    queryset = HireMe.objects.all()


class HireMeView(generics.CreateAPIView):
    serializer_class = HireMeSerializer
    permission_classes = (AllowAny,)

