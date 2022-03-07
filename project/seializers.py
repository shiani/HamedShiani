from rest_framework import serializers
from .models import Project, Tool, Category, ProjectImage


class ToolSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tool
        fields = "__all__"


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class ProjectImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectImage
        fields = ["image", ]


class ProjectSerializer(serializers.ModelSerializer):
    tools = ToolSerializer(many=True)
    category = CategorySerializer()

    class Meta:
        model = Project
        fields = ["title", "slug", "create_date", "client_name", "client_services", "client_website",
                  "client_phone_number",
                  "objective", "challenges", "category", "tools", "images", ]

    images = serializers.SerializerMethodField()

    def get_images(self, obj):
        images = obj.project_image.all()
        return ProjectImageSerializer(instance=images, many=True).data


class ProjectListSerializer(serializers.ModelSerializer):
    category = CategorySerializer()

    class Meta:
        model = Project
        fields = ["title", "slug", "category", "image", ]

    image = serializers.SerializerMethodField()

    def get_image(self, obj):
        image = obj.project_image.all().first()
        return ProjectImageSerializer(instance=image).data