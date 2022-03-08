from rest_framework import serializers
from .models import HireMeSubject, HireMe


class HireMeSubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = HireMeSubject
        fields = "__all__"


class HireMeSerializer(serializers.ModelSerializer):
    class Meta:
        model = HireMe
        fields = "__all__"
