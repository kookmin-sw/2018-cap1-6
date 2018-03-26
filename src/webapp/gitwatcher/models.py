from django.db import models
from django.utils import timezone
import datetime

# Create your models here.

class Githuburls(models.Model):
    github_url = models.CharField(max_length = 200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.github_url

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
