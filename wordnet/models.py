from django.db import models
from django.contrib.auth.models import User
import reversion

class Definition(models.Model):
    term = models.CharField(max_length=200, null=True)
    definition = models.TextField(null=True)
    lexical_id = models.CharField(max_length=300, null=True, blank=True)
    instance_of = models.ManyToManyField('self', null=True, related_name="parent_of", symmetrical=False, blank=True)
    domain = models.ForeignKey('Domain', null=True, blank=True)

    def __unicode__(self):
        return self.term

    def get_absolute_url(self):
        return "/wordnet/{}/".format(self.id)

class Domain(models.Model):
    name = models.CharField(max_length=300)

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return "/wordnet/domain/{}/".format(self.id)

#class Submission(models.Model):
#   term = models.CharField(max_length=200)
#   definition = models.TextField()
#   instance_of = models.ManyToManyField(Definition, null=True, symmetrical=False)
#   submitter = models.ForeignKey(User)