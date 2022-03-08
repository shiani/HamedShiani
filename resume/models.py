from django.db import models


def upload_resume_path(instance, filename):
    return f"about/{filename}"


class Resume(models.Model):
    file = models.FileField()
    create_date = models.DateTimeField(auto_now=True)
