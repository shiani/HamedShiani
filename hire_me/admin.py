from django.contrib import admin
from .models import HireMeSubject, HireMe

admin.site.register(HireMeSubject)


class HireMeAdmin(admin.ModelAdmin):
    list_display = ["full_name", "email", "subject"]
    list_filter = ["subject"]


admin.site.register(HireMe, HireMeAdmin)
