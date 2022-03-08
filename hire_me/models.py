from django.db import models


class HireMeSubject(models.Model):
    text = models.CharField(max_length=20)

    def __str__(self):
        return self.text


class HireMe(models.Model):
    full_name = models.CharField(max_length=38)
    email = models.EmailField()
    subject = models.ForeignKey(to=HireMeSubject, on_delete=models.CASCADE)
    description = models.TextField()

    def __str__(self):
        return self.full_name

