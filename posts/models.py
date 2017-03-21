from __future__ import unicode_literals
import datetime
from django.db import models
from django.utils import timezone
import os


def item_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
	#return 'item{0}/{1}'.format(instance.item_name, filename)
	
    ext = filename.split('.')[-1]
    filename = "%s/image1.jpg" % (instance.item_name)
    return os.path.join('.', filename)

# Create your models here.
class Item(models.Model):
	item_name = models.CharField(max_length=50)
	item_description = models.CharField(max_length=300)
	pub_date = models.DateTimeField('date published')
	link = models.CharField(max_length=300)
	price = models.DecimalField(max_digits=6, decimal_places=2)
	image = models.FileField(upload_to=item_directory_path, default='Patrick_DNA.jpeg')
#	image = models.FileField(upload_to='')
	def __str__(self):
		return self.item_name
	


    
	

#return later and add image(s) field
