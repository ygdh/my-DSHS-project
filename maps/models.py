from django.db import models

# Create your models here.
class Location(models.Model):
	name = models.CharField(max_length = 10)
	introduction = models.TextField()
	building = models.CharField(max_length = 15)
	floor_number = models.IntegerField(default = 0)

	def __str__(self):
		return self.name
class Show(models.Model):
	building = models.CharField(max_length = 15)
class See(models.Model):
	show = models.ForeignKey(Show, on_delete = models.CASCADE)
	location = models.ForeignKey(Location, on_delete = models.CASCADE)