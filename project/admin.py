from django.contrib import admin

from .models import Project, Tool, ProjectImage, Category


class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'create_date', 'client_name', 'is_active')
    list_editable = ('is_active',)


admin.site.register(Project, ProjectAdmin)


class ToolAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Tool, ToolAdmin)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Category, CategoryAdmin)

admin.site.register(ProjectImage)
