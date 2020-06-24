from django.db import models
from datetime import datetime

# Create your models here.


class Contact(models.Model):
    full_name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    subject = models.CharField(max_length=300)
    message = models.TextField(max_length=600)
    contact_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.subject + " by " + self.email


class Need_Help(models.Model):
    full_name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    subject = models.CharField(max_length=300)
    problem = models.TextField(max_length=600)
    need_help_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.subject + " by " + self.email
