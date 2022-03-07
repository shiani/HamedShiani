from django.http import Http404
from rest_framework import generics, filters
from rest_framework.permissions import AllowAny

from .models import Project
from .seializers import ProjectSerializer, ProjectListSerializer


class ProjectList(generics.ListAPIView):
    serializer_class = ProjectListSerializer
    permission_classes = (AllowAny,)
    filter_backends = [filters.SearchFilter]
    search_fields = ["title", "client_name", "client_services", "objective", "challenges", "category__name",
                     "tools__name"]

    def get_queryset(self):
        return Project.objects.filter(is_active=True)


class ProjectSingle(generics.RetrieveAPIView):
    serializer_class = ProjectSerializer
    permission_classes = (AllowAny,)

    def get_object(self):
        try:
            project = Project.objects.get(slug=self.kwargs.get('slug'))
            return project
        except Project.DoesNotExist:
            raise Http404()
