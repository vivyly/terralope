from django.db import models
from django.contrib.auth.models import User

class Rating(models.Model):
    service = models.IntegerField() #null ok, 1-5
    decor   = models.IntegerField() #null ok, 1-5
    product = models.IntegerField() #null ok, 1-5
    review  = models.TextField()
    revisit = models.BooleanField()
    reviewer = models.ForeignKey(User)
