from django.db import models
from django.contrib.auth.models import User

class Rating(models.Model):
    user = models.ForeignKey (User,on_delete=models.CASCADE)
    menuitem_id = models.SmallIntegerField()
    rating = models.SmallIntegerField()
    