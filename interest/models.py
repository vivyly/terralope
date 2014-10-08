from django.db import models

class InterestStatus(models.Model):
    status   = models.CharField() #choices=visited, upcoming, skip, other
    reason   = models.TextField()
    priority = models.IntegerField() #ramge: 1 to 5

class InterestType(models.Model):
    itype = models.CharField() #choices=restaurant, cafe, specialty_food, museum, site, monument, event)

class OpenHours(models.Model):
    day           = models.IntegerField() #1(Monday)-7(Sunday) day of the week
    start_time    = models.TimeField()
    end_time      = models.TimeField()
    past_midnight = models.BooleanField() #not sure if needed

class Interest(models.Model):
    interest_type = models.ForeignKey(InterestType)
    status        = models.ForeignKey(InterestStatus)
    name          = models.CharField()
    point         = models.ForeignKey(LatLong)
    city          = models.ForeignKey(City)
    cost          = models.FloatField()
    rating        = models.ForeignKey(Rating)
    desc          = models.TextField()
    open_hours    = models.ForeignKey(OpenHours)
    hours_spent   = models.FloatField()
    wait_time     = models.FloatField()
    preorder      = models.BooleanField()

class Visited(models.Model):
    interest = models.ForeignKey(Interest)
    datetime = models.DateTimeField()
    duration = models.FloatField()

#might add a upcoming/planned class for planning trips

