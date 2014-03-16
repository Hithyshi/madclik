#from django.db import models

# Create your models here.

from django.db import models

# Create your models here.

class CustomerAdvertise(models.Model):
  custname = models.CharField(max_length=200)
  description = models.TextField(max_length=1000)
  def __unicode__(self):
    return self.custname, self.description
