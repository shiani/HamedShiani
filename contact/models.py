from django.db import models


class ContactForm(models.Model):
    full_name = models.CharField(max_length=38)
    email = models.EmailField()
    subject = models.CharField(max_length=64)
    message = models.TextField()

    def __str__(self):
        return self.full_name


class ContactDetails(models.Model):
    address = models.TextField()
    email = models.EmailField()
    phone_number = models.CharField(max_length=11)

    def __str__(self):
        return self.email
