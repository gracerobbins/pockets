from __future__ import unicode_literals
import datetime
from django.db import models
from django.utils import timezone

# Create your models here.
class Item(models.Model):
	item_name = models.CharField(max_length=50)
	item_description = models.CharField(max_length=300)
	pub_date = models.DateTimeField('date published')
	link = models.CharField(max_length=300)
	price = models.DecimalField(max_digits=6, decimal_places=2)
	def __str__(self):
		return self.item_name

#return later and add image(s) field
