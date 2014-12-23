from django.db import models
from django.contrib.auth.models import User
from wordnet.models import Definition
from djangoratings.fields import RatingField

class Experience(models.Model):
    user = models.ForeignKey(User)
    type = models.ForeignKey(Definition)
    
    
class Resource(models.Model):
    name = models.CharField(max_length=200)
    type = models.ForeignKey(Definition)

    def get_absolute_url(self):
        return '/experience/resource/{}/'.format(self.id)

class Involvement(models.Model):
    experience = models.ForeignKey(Experience)
    resource = models.ForeignKey(Resource)
    role = models.ForeignKey(Definition)

class Camp(Resource):
    description = models.TextField()
    url = models.URLField(max_length=500)
    address = models.CharField(max_length=500)
    longitude = models.FloatField(null=True)
    latitude = models.FloatField(null=True)
    rating = RatingField(range=5)

    def __unicode__(self):
        return self.name

class TextRating(models.Model):
    camp = models.ForeignKey(Camp)
    user = models.ForeignKey(User)
    text = models.TextField()
