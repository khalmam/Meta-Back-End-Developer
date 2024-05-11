from django.db import models

# Create your models here.
class Reservation(models.Model):
    name = models.CharField(max_length=100, blank=True)
    contact = models.CharField('Phone Number' ,max_length=200)
    guest_count	= models.IntegerField()
    time = models.TimeField()
    notes= models.CharField(max_length=300, blank=True)

    def __str__(self):
        return self.name