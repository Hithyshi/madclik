#from django.db import models

# Create your models here.

from django.db import models
import datetime
from django.utils import timezone

# Create your models here.

class CustomerAdvertise(models.Model):
  custname = models.CharField(max_length=200)
  description = models.TextField(max_length=1000)
  def __unicode__(self):
    return self.custname, self.description


class CustomerAdvertise2(models.Model):
  item_cat = models.CharField(max_length=30)
  item_subcat = models.CharField(max_length=40, blank=True)
  item_name = models.CharField(max_length=40)
  item_desc = models.TextField(max_length=200)
  item_price = models.IntegerField(default=0)
  item_price_per = models.CharField(max_length=20, blank=False)
  item_sec_dep = models.IntegerField(default=0)
  item_tandc = models.TextField(max_length=300)
  item_owner_type = models.CharField(max_length=30)
  item_owner_name = models.CharField(max_length=30)
  item_owner_email = models.CharField(max_length=50)
  item_mobile_num = models.IntegerField(blank=False)
  state = models.CharField(max_length=20)
  city = models.CharField(max_length=20)
  locality = models.CharField(max_length=40)

