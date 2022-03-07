from django.db import models


def upload_news_image_path(instance, filename):
    return f"about/{filename}"


class AboutMe(models.Model):
    image = models.ImageField(upload_to=upload_news_image_path)
    description = models.TextField()
    years_of_experience = models.SmallIntegerField()
    projects_completed = models.SmallIntegerField()
    first_name = models.CharField(max_length=10)
    last_name = models.CharField(max_length=10)

    def __str__(self):
        return self.first_name + " " + self.last_name

