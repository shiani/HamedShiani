from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse


def upload_news_image_path(instance, filename):
    return f"project/{filename}"


class Category(models.Model):
    name = models.CharField(max_length=150)
    slug = models.SlugField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('', kwargs={'slug': self.slug})

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)


class Tool(models.Model):
    name = models.SlugField(max_length=150)
    slug = models.SlugField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('', kwargs={'slug': self.slug})

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)


class Project(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(null=True, blank=True)
    create_date = models.DateField(auto_now_add=True)
    client_name = models.CharField(max_length=255, blank=True, null=True)
    client_services = models.CharField(max_length=511, blank=True, null=True)
    client_website = models.URLField(blank=True, null=True)
    client_phone_number = models.CharField(max_length=11, blank=True, null=True)
    objective = models.TextField(blank=True, null=True)
    challenges = models.TextField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    category = models.ForeignKey(to=Category, on_delete=models.PROTECT, blank=True, null=True)
    tools = models.ManyToManyField(to=Tool)

    def __str__(self):
        return self.title

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)


class ProjectImage(models.Model):
    image = models.ImageField(upload_to=upload_news_image_path)
    project = models.ForeignKey(to=Project, on_delete=models.CASCADE, related_name='project_image')

    def __str__(self):
        return self.project.title
