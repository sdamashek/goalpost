from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.ForeignKey(User, unique=True)
    address = models.CharField(max_length=500)
    radius = models.FloatField()
    maximum_cost = models.FloatField()
    phone_number = models.CharField(max_length=15)

User.profile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])