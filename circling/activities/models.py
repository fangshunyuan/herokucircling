from django.db import models


class Activities(models.Model):
	title = models.CharField(max_length=50)
	pub_date = models.DateTimeField('date published')
	time = models.DateTimeField('time of activity')
	location = models.CharField(max_length=200)
	max_pax = models.IntegerField(default=0)
	cost = models.IntegerField(default=0)
	curr_pax = models.IntegerField(default=0)
	description = models.CharField(max_length=200)

	def __unicode__(self):              # __unicode__ on Python 2
		return self.title