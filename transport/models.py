from django.db import models

class TransportType(models.Model):
    name = models.CharField() #choices=walk, public, private, tour, drive
    preorder       = models.BooleanField()
    cost           = models.TextArea()
    desc           = models.TextArea()
    review         = models.TextArea()

class Transport(models.Model):
    transport_type = models.ForeignKey(TransportType)
    distance       = models.FloatField()
    start          = models.ForeignKey(LatLong) # starting point
    end            = models.ForeignKey(LatLong) # ending point
    time_spent     = models.FloatField()
    cost           = models.FloatField()
