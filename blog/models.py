from django.db import models
from django.contrib.auth.models import User

class Article(models.Model):
    slug    = models.SlugField(max_length=10)
    creator = models.ForeignKey(User)
    title   = models.CharField(max_length=255)
    dek     = models.TextField()
    content = models.TextField()
